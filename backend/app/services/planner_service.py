class PlannerService:

    def create_cad_workflow(self):

        return [
            {
                "task_name": "Requirements Analysis",
                "agent": "planner-agent"
            },
            {
                "task_name": "Engineering Design",
                "agent": "cad-agent"
            },
            {
                "task_name": "Geometry Generation",
                "agent": "cad-agent"
            },
            {
                "task_name": "Export STEP",
                "agent": "cad-agent"
            },
            {
                "task_name": "QA Validation",
                "agent": "qa-agent"
            }
        ]


planner_service = PlannerService()