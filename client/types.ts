export interface Answer {
    key: string
    text: string
}

export interface Question {
    key: string
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
    key: string
    name: string
    trials: Trial[]
}