export interface Answer {
    key: string
    text: string
}

export interface Question {
    question: string
    prompt: string
    answers: Answer[]
    correct_answer: Answer
}

export interface Trial {
    key: string
    question: Question
}

export interface Experiment {
    name: string
    trials: Trial[]
}