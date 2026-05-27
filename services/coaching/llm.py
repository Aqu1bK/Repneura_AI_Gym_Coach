from openai import OpenAI
import os
from services.config.workout_config import PROMPT


class LLMCoach:
    def __init__(self, openrouter_client):
        self.client = openrouter_client
        self.history = []
        self.system_prompt = PROMPT
        # Use a free Qwen model from OpenRouter
        self.model = "qwen/qwen-2.5-7b-instruct"

    def give_feedback(self, event, issue):
        prompt = f"Event: {event}"

        if issue:
            prompt += f" Form Issue: {issue}"

        messages = [
            {"role": "system", "content": self.system_prompt},
            *self.history[-10:],
            {"role": "user", "content": prompt}
        ]

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.4,
            max_tokens=150,
        )

        text = response.choices[0].message.content.strip()
        self.history.append({"role": "assistant", "content": text})

        return text
    