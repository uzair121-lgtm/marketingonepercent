# Measurement & attribution

**Target: 100% of installs attributable to an ad set.**

## Activation event — CONFIRM WITH FOUNDER BEFORE REPORTING
A canary user = install **+ completed first-run setup**, marked by the event **`first_run_complete`** (founder-confirmed 2026-07-27). All canary counts report against this event.

- Event name: `first_run_complete`
- Confirmed: ☑  Date: 2026-07-27  Event: `first_run_complete` (founder-confirmed)

## End-to-end test — must PASS by 14 Aug
Nothing ships to the store until this passes; the SDK must be in the submitted binary.

- ☐ Meta SDK in the build
- ☐ App events firing (install + activation event)
- ☐ SKAdNetwork configured
- ☐ ATT prompt in place
- ☐ Test install attributes end-to-end to the correct ad set

**Escalate immediately if the test fails after 14 Aug.**

## Reporting basis
Every canary user is attributed to a source (paid ad set, or a named free channel). Paid installs must map to an ad set; free installs carry the `source` field from `tracking/leads.csv`.
