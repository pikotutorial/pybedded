class Servo:
    def attach(self, pin: int) -> None:
        pass

    def write(self, value: int) -> None:
        pass

    def writeMicroseconds(self, value: int) -> None:
        pass

    def read(self) -> int:
        return 0
    
    def attached(self) -> bool:
        return False
    
    def detach(self) -> None:
        pass
