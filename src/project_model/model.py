from mesa import Agent, Model


# A user with preferences for different trends
class User(Agent):
    def __init__(self, model, preferences):
        super().__init__(model)
        self.preferences = preferences
        self.adjusted_preferences = {}

    # Calculate this user's personal score for a trend
    def get_personal_score(self, trend_name):
        preference = self.preferences[trend_name]

        return preference * 5 - 5 * (3 - preference)


# A trend that receives feedback from users
class Trend(Agent):
    def __init__(self, model, name):
        super().__init__(model)
        self.name = name
        self.score = 0
        self.average = 0

    def calculate_score(self):
        personal_scores = []

        # Calculate each user's original score
        for user in self.model.users:
            num = user.preferences[self.name]

            num = num * 5 - 5 * (3 - num)

            personal_scores.append(num)

        # Calculate the average score for this trend
        average = sum(personal_scores) / len(personal_scores)

        # Apply sensitivity to EACH user's score
        adjusted_scores = []

        for num in personal_scores:
            adjusted_score = num + (average * self.model.sensitivity)
            adjusted_scores.append(adjusted_score)

        # Save the adjusted scores for each user
        for user, adjusted_score in zip(self.model.users, adjusted_scores):
            user.adjusted_preferences[self.name] = adjusted_score

        # Calculate the overall trend score
        self.score = sum(adjusted_scores) / len(adjusted_scores)

        self.average = average

# The main simulation
class SocialMediaModel(Model):
    def __init__(self, sensitivity):
        super().__init__()

        self.sensitivity = sensitivity

        # Three users with scores from 0-3
        self.users = [
            User(self, {"fitness": 2, "cooking": 3, "gaming": 3}),
            User(self, {"fitness": 3, "cooking": 0, "gaming": 1}),
            User(self, {"fitness": 1, "cooking": 1, "gaming": 0})
        ]

        self.trends = [
            Trend(self, "fitness"),
            Trend(self, "cooking"),
            Trend(self, "gaming")
        ]

    def step(self):

        # Calculate adjusted scores for every trend
        for trend in self.trends:
            trend.calculate_score()

        # Display each user's adjusted trend scores
        print("\nAdjusted User Trend Scores:")

        for i, user in enumerate(self.users):
            print(f"\nUser {i + 1}:")

            # Sort this user's trends from highest to lowest
            sorted_trends = sorted(
                self.trends,
                key=lambda trend: user.adjusted_preferences[trend.name],
                reverse=True
            )

            for rank, trend in enumerate(sorted_trends, start=1):
                score = user.adjusted_preferences[trend.name]

                print(f"  {rank}. {trend.name.capitalize()}: {score:.2f}")

        # Sort overall trends from highest to lowest
        rankings = sorted(
            self.trends,
            key=lambda trend: trend.score,
            reverse=True
        )

        print("\nOverall Trend Rankings:")

        for i, trend in enumerate(rankings):
            print(
                f"{i + 1}. {trend.name.capitalize()} "
                f"= {trend.score:.2f} "
                
            )

# BASELINE
print("\n========== BASELINE (Sensitivity = 0) ==========")
baseline = SocialMediaModel(0)
baseline.step()

# ALTERNATIVE 1
print("\n========== ALTERNATIVE (Sensitivity = 1) ==========")
alternative = SocialMediaModel(1)
alternative.step()

# ALTERNATIVE 2
print("\n========== ALTERNATIVE (Sensitivity = 2) ==========")
alternative2 = SocialMediaModel(2)
alternative2.step()