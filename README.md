# Langgraph-Learnings
Langgraph mini projects for learning.

Agentic AI characterstics:
1. Autonomous
2. Goal Oriented
3. Planning
4. Reasoning
5. Adaptability
6. Context Awareness

1. Autonomy: Refers to AI system's abality to make decision and take actions on its own to acheive a goal on its own.
Execution
Decision Making
Tool Usage

2. Goal Oriented: AI system operates with a persistant objective in mind and continously directs its action towards it.

3. Planning: Agent's ability to break down high-level goal into a structured sequence of actions or subgoals and decide best path to acheive the desired goal.

4. Reasoning: cognitive process through which an agentic ai system interprets infor draws conclusion and make decision. 
a. Planning during Execution.
b. Reasoning during Execution.

5. Adaptability: Agent's ability to modify its plans, strategies or actions in response to unexpected conditions.

6. Context awareness: agent's ability to understand, retrain and utilize relevant information form ongoing task, past interactions, user preferences, and env ues to make better decision throughout a multi step process. Short Term Memory and Long Term Memory.


Agentic AI Components:

1. Brain
2. Orchestrator
3. Tools
4. Memory
5. Supervisor


Agent and workflow difference:
1. Workflows are systems where LLMs and tools are orchestrated through predefined code paths.
2. Agent are systems where LLMs dyamically direct their own processes and tool usage maintaining control over how they accomplish tasks.

Challenge with langchain:
1. We need to write Lots of Glue code for complex agentic workflows.
2. Langgraph provide handling state internally which is maintained throughout the workflow which langchain do not provide.
3. Event driven Execution: langchain is sequential but langgraph can pause the workflow wait for trigger and move on.
4. Fault tolerance: long riunning workflow rises faults and langchain do not provide any fault tolerance supports. Langgraph gives you option to retry and handle small level fault and recovery for long running fault like server down. example user checkpointer to save sates.
5. Human in the loop.
6. Nested workflows: adding subgraphs.
7. Observability: by directly integrating Langsmith.


Types of Workflows
1. Prompt chaining.
2. Routing
3. Parallellization.
4. Orchestrator Workers.
5. Evaluatior Opimizer.