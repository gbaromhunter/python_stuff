import sounddevice as sd
import soundfile as sf


with sf.SoundFile(self.filepath,
                  mode='x',
                  samplerate=self.SAMPLE_RATE,
                  channels=self.CHANNELS,
                  subtype=None) as file:
    with sd.InputStream(samplerate=self.SAMPLE_RATE, device=self.mic_id,
                        channels=self.CHANNELS, callback=self.callback):
        logger.info(f"New recording started: {self.sound_file.name}")
        try:
            while True:
                file.write(self.mic_queue.get())

        except RuntimeError as re:
            logger.debug(f"{re}. If recording was stopped by the user, then this can be ignored")


    def callback(self, indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        self.mic_queue.put(indata.copy())


    def pause_recording(self):
        """Mimics a 'pause' functionality by writing the current sound file changes to disk.
        Upon 'resume' a new recording will be made. Note: close() is not called here, because
        that would kill the recording thread
        """
        self.sound_file.flush()
        logger.info(f"'Paused' (closed) recording: {self.sound_file.name}")


    def resume_recording(self):
        """
        Mimics 'resuming' by starting a new recording, which will be merged with the others
        when the user selects Stop & Save (or deleted upon Stop & Delete)
        Note: get_full_sound_file_name() outputs a new recording with the same base name as the first, but appends a
        `_part2` or `_part3` etc. to the suffix to distinguish it from the first and maintain order.
        """
        self.sound_file = self.get_full_sound_file_name()
        self.record()


    def stop_mic_recording(self):
        try:
            self.sound_file.flush()
            self.sound_file.close()
            logger.info(f"Stopped and closed recording: {self.sound_file.name}")

        except RuntimeError as e:
            logger.info(f"Error stopping/saving {self.sound_file.name}. Make sure the file exists and can be modified")
            logger.info(f"RunTimeError: \n{e}")


    def combine_recordings_if_needed(self):
        """
        If recording was paused, combines all sections in alphabetical order into a new audio file
        """
        if self.section_count > 1:  # this is incremented when a recording is paused/resumed
            combined_audio = AudioSegment.empty()
            files_combined = []
            for rec in glob.glob(os.path.join(RECORDING_DIR, "*" + self.FILE_EXT)):
                combined_audio = combined_audio + AudioSegment.from_wav(
                    rec)  # this is why alphabetical order is important
                files_combined.append(rec)
            combined_file_name = os.path.join(RECORDING_DIR, self.base_filename + "_combined" + self.FILE_EXT)
            combined_audio.export(out_f=combined_file_name, format="wav")
            logger.info(f"Combined the following recordings into {combined_file_name}:"
                        f"\n {files_combined}")
