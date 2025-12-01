from backend.agents import LifestyleAgent

def test_agent():
    agent = LifestyleAgent()
    output = agent.generate_plan({"goal": "test"})
    assert "data" in output

