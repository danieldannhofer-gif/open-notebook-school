"""
Domain models for Learning Materials - Flashcard & Quiz Support.

This module contains the domain models for flashcard decks, flashcards, flashcard reviews,
quizzes, quiz questions, quiz attempts, and quiz answers.
"""

from datetime import datetime
from typing import ClassVar, List, Literal, Optional

from pydantic import Field

from open_notebook.domain.base import ObjectModel


class FlashcardDeck(ObjectModel):
    """Represents a collection of flashcards organized around a topic or subject."""
    
    table_name: ClassVar[str] = "flashcard_deck"
    name: str
    description: str = ""
    notebook: str  # RecordID of Notebook
    created: datetime = Field(default_factory=datetime.now)
    updated: datetime = Field(default_factory=datetime.now)
    tags: List[str] = Field(default_factory=list)


class Flashcard(ObjectModel):
    """Represents an individual flashcard with a question and answer."""
    
    table_name: ClassVar[str] = "flashcard"
    deck: str  # RecordID of FlashcardDeck
    question: str
    answer: str
    position: int = 0
    quality_score: float = Field(default=1.0, ge=0.0, le=1.0)
    is_approved: bool = True
    created: datetime = Field(default_factory=datetime.now)


class FlashcardReview(ObjectModel):
    """Represents a user's review/attempt of a flashcard."""
    
    table_name: ClassVar[str] = "flashcard_review"
    flashcard: str  # RecordID of Flashcard
    user_token: str
    is_correct: bool
    reviewed_at: datetime = Field(default_factory=datetime.now)


class Quiz(ObjectModel):
    """Represents a quiz or test with multiple questions."""
    
    table_name: ClassVar[str] = "quiz"
    name: str
    description: str = ""
    notebook: str  # RecordID of Notebook
    created: datetime = Field(default_factory=datetime.now)
    updated: datetime = Field(default_factory=datetime.now)


class QuizQuestion(ObjectModel):
    """Represents an individual question within a quiz."""
    
    table_name: ClassVar[str] = "quiz_question"
    quiz: str  # RecordID of Quiz
    question: str
    question_type: Literal["multiple_choice", "true_false", "short_answer", "fill_blank"]
    options: List[str] = Field(default_factory=list)
    correct_answer: str
    explanation: str = ""
    points: int = 1
    position: int = 0
    quality_score: float = Field(default=1.0, ge=0.0, le=1.0)
    is_approved: bool = True
    created: datetime = Field(default_factory=datetime.now)


class QuizAttempt(ObjectModel):
    """Represents a user's attempt at taking a quiz."""
    
    table_name: ClassVar[str] = "quiz_attempt"
    quiz: str  # RecordID of Quiz
    user_token: str
    started_at: datetime = Field(default_factory=datetime.now)
    completed_at: Optional[datetime] = None
    score: Optional[float] = None


class QuizAnswer(ObjectModel):
    """Represents a user's answer to a specific quiz question."""
    
    table_name: ClassVar[str] = "quiz_answer"
    attempt: str  # RecordID of QuizAttempt
    question: str  # RecordID of QuizQuestion
    user_answer: str
    is_correct: bool
    reviewed: bool = False


# Export all classes
__all__ = [
    "FlashcardDeck",
    "Flashcard", 
    "FlashcardReview",
    "Quiz",
    "QuizQuestion",
    "QuizAttempt",
    "QuizAnswer",
]