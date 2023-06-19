class MediaPlayer:
    def play(self, audio_type, filename):
        pass

class AdvancedMediaPlayer:
    def play_vlc(self, filename):
        pass

    def play_mp4(self, filename):
        pass

class VLCPlayer(AdvancedMediaPlayer):
    def play_vlc(self, filename):
        print("Playing VLC file:", filename)

class MP4Player(AdvancedMediaPlayer):
    def play_mp4(self, filename):
        print("Playing MP4 file:", filename)

class MediaAdapter(MediaPlayer):
    def __init__(self, audio_type, filename):
        if audio_type == "vlc":
            self.advanced_player = VLCPlayer()
        elif audio_type == "mp4":
            self.advanced_player = MP4Player()
        self.filename = filename

    def play(self, audio_type, filename):
        if audio_type == "vlc":
            self.advanced_player.play_vlc(self.filename)
        elif audio_type == "mp4":
            self.advanced_player.play_mp4(self.filename)

class AudioPlayer(MediaPlayer):
    def play(self, audio_type, filename):
        if audio_type == "mp3":
            print("Playing MP3 file:", filename)
        elif audio_type == "vlc" or audio_type == "mp4":
            media_adapter = MediaAdapter(audio_type, filename)
            media_adapter.play(audio_type, filename)
        else:
            print("Invalid media type:", audio_type)

# Usage
audio_player = AudioPlayer()
audio_player.play("mp3", "song.mp3")
audio_player.play("vlc", "movie.vlc")
audio_player.play("mp4", "video.mp4")
audio_player.play("avi", "video.avi")
