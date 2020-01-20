from metaflow import FlowSpec, Parameter, step


class SilicoSpec(FlowSpec):
    
    my_data = Parameter('data', default=1)

    @step
    def start(self):
        self.population = [self.my_data] * 20

        self.next(self.end)

    @step
    def end(self):
        print(self.population)


if __name__ == "__main__":
    SilicoSpec()