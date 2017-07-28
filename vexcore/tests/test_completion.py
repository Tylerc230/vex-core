from vexcore.completion import Completion
class TestCompletion():
    def test_completion(self):
        completion = Completion(text="let a = ")
        options = completion.completion_at_offset(5)
        print(options)


