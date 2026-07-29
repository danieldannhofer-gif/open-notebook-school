# Open Notebook School

A classroom learning tool built on Open Notebook. Teachers and pupils author learning materials — flashcards and quizzes — from sources, with pupils able to create and share their own.

## Language

**Generation Pipeline**:
The shared machinery that turns a Source plus a prompt into LLM output. Used by transformations, flashcard generation, and quiz generation alike.
_Avoid_: transformation (when you mean the pipeline rather than the record)

**Transformation**:
A record holding a user-authored, free-text prompt that is run over a Source through the Generation Pipeline. Its output is an unvalidated Insight.
_Avoid_: template, preset

**Fixed Prompt**:
An app-authored, non-editable prompt used by the Generation Pipeline to produce typed records. Distinguished from a Transformation by who writes it: the application, not the user.
_Avoid_: system prompt, built-in transformation

**Insight**:
The untyped string output of running a Transformation over a Source.
_Avoid_: result, output

**Flashcard**:
A typed, addressable record with a question and an answer, produced by the Generation Pipeline from a Fixed Prompt. Addressable because a Review must reference it.
_Avoid_: card, note

**Quiz Question**:
A typed, addressable record with a question, a question type, options, and a correct answer. Addressable because an Answer must reference it.
_Avoid_: question (unqualified)
