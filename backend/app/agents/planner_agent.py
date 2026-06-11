class PlannerAgent:

    def generate_cad_tasks(self):

        return [
            {
                "task": "Requirements Analysis",
                "agent": "planner-agent"
            },
            {
                "task": "Engineering Design",
                "agent": "cad-agent"
            },
            {
                "task": "Geometry Creation",
                "agent": "cad-agent"
            },
            {
                "task": "STEP Export",
                "agent": "cad-agent"
            },
            {
                "task": "QA Validation",
                "agent": "qa-agent"
            }
        ]


planner_agent = PlannerAgent()