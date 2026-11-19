# UCI Degree Graph Visualizer
Plan your UCI degree as a map instead of a checklist. Pick a major and catalog year, and the app builds your full set of requirements as a graph: prerequisite chains, "choose 2 of these" groups, and everything still left to take. Mark prerequisite courses as complete and the courses they unlock light up, while the ones still blocked stay greyed out, so you can see what to take next and what's holding up the rest of your degree.

*Unofficial student project. Not affiliated with UC Irvine. Course and requirement data comes from [Anteater API](https://anteaterapi.com).*
## Features
### MVP
-  Choose a major and catalog year
-  Render the major's requirements as an interactive graph (prerequisite chains, "choose N of these" groups)
-  Click a course to mark it complete
-  Lock and unlock courses automatically based on completed prerequisites
-  Show progress on each requirement (e.g. 3 of 11 upper-division electives)
-  Save progress in the browser between visits
-  Support the specialization picker for majors that require one
  
## Architecture
```text
Anteater API <-- Ingestion job --> PostgreSQL <-- FastAPI <-- React
   (fetch)          (upsert)                       (read)      (HTTP/JSON)
```
Ingestion (fetch from AnteaterAPI) happens offline, quarterly, to track and update course or other changes. At request time, users never make requests directly to the AnteaterAPI, that data is already stored in Postgres. Prerequisite evaluations happen right on the React frontend, the API sends the full course requirement tree to the frontend and each click computes and changes UI instantly. User course progress only lives in the browser, backend is read-only and stateless. No user accounts in the MVP. 

## Tech Stack

### Backend
- **FastAPI**: Pydantic models validate and serialize the JSON the API serves, and the auto-generated Swagger UI allows endpoint testing without a frontend
- **PostgreSQL**: Stores relational tables for courses and requirements, matching what is used in production
- **SQLAlchemy and Alembic**: SQLAlchemy maps tables to Python classes; Alembic versions every schema change
- **Docker/Docker compose**: Ensure development and/or production environment are consistent
- **React/Vite**: Faster frontend development, fast response and UI re-render during changes

## 
## 
## 
## 
## 
