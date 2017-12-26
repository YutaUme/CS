class Config:
    __PopulationSize = 50 # Population Size
    __MaxDomain = 500 # variable upper limit
    __MinDomain = -500 # variable lower limit
    __Lambda = 1.5 # parameter for Levy flight
    __Pa = 0.25
    __Step_Size = 0.01
    __Dimension = 10 # The number of dimension
    __Trial = 31
    __Iteration = 3000

    @classmethod
    def get_population_size(cls):
        return cls.__PopulationSize

    @classmethod
    def get_Pa(cls):
        return cls.__Pa

    @classmethod
    def get_iteration(cls):
        return cls.__Iteration

    @classmethod
    def get_trial(cls):
        return cls.__Trial

    @classmethod
    def get_dimension(cls):
        return cls.__Dimension

    @classmethod
    def get_max_domain(cls):
        return cls.__MaxDomain

    @classmethod
    def set_max_domain(cls, _max_domain):
        cls.__MaxDomain = _max_domain

    @classmethod
    def get_min_domain(cls):
        return cls.__MinDomain

    @classmethod
    def set_min_domain(cls, _min_domain):
        cls.__MinDomain = _min_domain

    @classmethod
    def get_lambda(cls):
        return cls.__Lambda

    @classmethod
    def set_lambda(cls, _lambda):
        cls.__Lambda = _lambda

    @classmethod
    def get_stepsize(cls):
        return cls.__Step_Size



