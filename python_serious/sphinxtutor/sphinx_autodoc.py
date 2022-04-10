"""
설명
=====
이 모듈은 문서화 테스트를 위한 모듈입니다.

Revision History
-----------------
 * [2022/04/10] - 모듈 작성    
"""

class Math(object):
    """두 개의 int 값을 입력받아 다양한 연산을 할 수 있도록 하는 클래스
    
    :param int a: a 값
    :param int b: b 값
    """

    def __init__(self, a, b):
        self._a = a
        self._b = b

    def sum(self):
        """미리 입력받은 a와 b값을 더한 결과를 반환합니다.

        예제:

            >>> Math(1, 2).add()
            3
        
        :returns int: a + b 에 대한 결과
        """
        return self._a + self._b
    
    def subtract(self):
        """미리 입력받은 a와 b값을 뺀 결과를 반환합니다.
   
        예제:

            >>> Math(2, 1).subtract()
            1
        
        :returns int: a - b 에 대한 결과
        """
        return self._a - self._b