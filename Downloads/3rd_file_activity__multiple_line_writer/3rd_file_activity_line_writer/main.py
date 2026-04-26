from recorder_logic import LifeRecorder

def start_app():
    # Gagawa tayo ng instance ng class
    app = LifeRecorder()
    # Patatakbuhin natin ang method
    app.write_multiple_lines()

if __name__ == "__main__":
    start_app()