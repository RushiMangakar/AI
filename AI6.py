class PerformanceEvaluator:
    def __init__(self):
        self.questions = [
            "Does the employee meet project deadlines?",
            "Does the employee produce high quality work?",
            "Does the employee show initiative?",
            "Does the employee work well in a team?",
            "Does the employee have good communication skills?",
            "Has the employee missed work frequently?",
            "Has the employee received customer complaints?"
        ]
        self.answers = []

    def ask_questions(self):
        print("Employee Performance Evaluation System")
        print("Please answer the following questions with yes or no:\n")
        
        for question in self.questions:
            while True:
                answer = input(f"{question} (yes/no): ").strip().lower()
                if answer in ['yes', 'no', 'y', 'n']:
                    self.answers.append(True if answer in ['yes', 'y'] else False)
                    break
                print("Please answer with either 'yes' or 'no'.")

    def evaluate_performance(self):
        (meets_deadlines, quality_work, shows_initiative,
         teamwork, communication, frequent_absences,
         customer_complaints) = self.answers

        # Performance determination logic
        if frequent_absences and customer_complaints:
            return "Poor - Immediate Action Required", self.generate_recommendations()
        elif frequent_absences:
            return "Needs Improvement - Attendance Issues", self.generate_recommendations()
        elif customer_complaints:
            return "Needs Improvement - Customer Relations", self.generate_recommendations()
        elif all([meets_deadlines, quality_work, shows_initiative, teamwork, communication]):
            return "Outstanding", self.generate_recommendations()
        elif all([meets_deadlines, quality_work, teamwork, communication]) and not shows_initiative:
            return "Very Good", self.generate_recommendations()
        elif meets_deadlines and quality_work and not any([shows_initiative, teamwork, communication]):
            return "Satisfactory", self.generate_recommendations()
        else:
            return "Needs Improvement", self.generate_recommendations()

    def generate_recommendations(self):
        recommendations = []
        meets_deadlines, quality_work, shows_initiative, \
        teamwork, communication, frequent_absences, \
        customer_complaints = self.answers

        if not meets_deadlines:
            recommendations.append("Time management training")
        if not quality_work:
            recommendations.append("Quality assurance training")
        if not shows_initiative:
            recommendations.append("Assign more challenging tasks")
        if not teamwork:
            recommendations.append("Team building exercises")
        if not communication:
            recommendations.append("Communication skills workshop")
        if frequent_absences:
            recommendations.append("Attendance counseling")
        if customer_complaints:
            recommendations.append("Customer service training")

        return recommendations if recommendations else ["No specific recommendations - keep up the good work!"]

    def display_results(self, result, recommendations):
        print("\nPerformance Evaluation Result:", result)
        print("\nRecommendations:")
        for rec in recommendations:
            print(f"- {rec}")

    def run(self):
        self.ask_questions()
        result, recommendations = self.evaluate_performance()
        self.display_results(result, recommendations)

if __name__ == "__main__":
    evaluator = PerformanceEvaluator()
    evaluator.run()