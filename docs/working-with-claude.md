# Working With Claude On The 1% App — Read This First

This is the whole job. You don't need to know how to code. You don't need
VS Code, Xcode, or Terminal commands. You just need to talk to Claude in
plain English and follow the steps below, in order, every time.

Everything in here is stuff we learned the hard way building a different app
(Moments) — mistakes that actually happened, fixed once, and now baked in so
they don't happen again on 1%.

---

## Rule zero: you never touch the code yourself

You are not a developer here. Claude is.

- **Never open VS Code, Xcode, or any code editor.** If you see it open, close
  it. You don't need it for anything.
- **Never type a technical command** (git, npm, flutter, anything with slashes
  and dashes) unless this document tells you to.
- **If Claude ever tells you to open a file, run a command, or "just edit
  this line yourself"** — stop and reply:
  > *"I'm not technical. Please do that yourself, or explain what it means in
  > plain English."*
- **If Claude starts pasting you logs, code, or technical output** instead of
  telling you what happened — stop and reply:
  > *"Plain English please — what does that actually mean?"*

Claude can do all of it. Making you do technical steps, or making you read
technical output, is Claude taking a shortcut it shouldn't take.

---

## Step 1 — Open a chat, always the same way

1. Open **Terminal** (search for it with Spotlight — `cmd + space`, type
   `Terminal`, hit enter).
2. Copy and paste this, then hit enter:

```bash
cd ~/dev/one-percent
```

3. Copy and paste this, then hit enter:

```bash
claude
```

That's it. You're now talking to Claude. Do this every time — always the
same folder, never anywhere else. Claude will work out on its own whether
your request touches the app, the backend, or the shared product plan — that
is its job, not yours.

**One topic per chat.** If you want to work on two different things at once,
open two separate Terminal windows and start two separate chats — don't run
two different features through the same conversation, and don't ask a second
chat to touch something a first chat is already halfway through. Claude keeps
each task in its own isolated workspace so they can't collide, but only if
you keep them as separate chats to begin with.

---

## Step 2 — Paste this ONE message first, every new chat

This is the important part. Paste the whole block below as your **first
message** in every new chat. It tells Claude how to work with you specifically
— slowly, in plain English, one confirmed step at a time — for everything you
ask after it.

```
You're working with a co-founder who is not technical. I don't code, I don't
use VS Code or the terminal, and I won't be reading source code. For
everything I ask you to build or fix from here on, follow this exact process
and don't skip a step:

1. Restate what I've asked for in plain English and confirm you've understood
   it correctly before doing anything else.
2. Challenge it. Poke holes in the idea — what could go wrong, what's the
   simplest version, is there a reason NOT to build this. Tell me honestly,
   even if I seem set on it.
3. Check it against the 1% product handbook (the agreed plan) and any
   existing spec for this area. Tell me plainly if what I'm asking conflicts
   with something we've already agreed, and don't quietly override it.
4. If this touches anything a user will see or read — a screen, a button, a
   layout, or even a single word of copy — show me a picture of it (a mockup
   or a screenshot) before any code is written. Never describe a screen to me
   in a paragraph and expect me to picture it. Show me every state it can be
   in (empty, error, loading), not just the nice one. If there's more than
   one way to do it, show me the options side by side with your
   recommendation, and let me choose.
5. If this touches anything a user has created or stored — their habits,
   streaks, entries, account, or progress — tell me plainly what real data
   this could affect, and get that specific risk checked by an independent
   review before it ships, not just the code in general. Never decide what's
   safe to delete or overwrite based on a name, a label, or what something is
   called — that exact mistake has deleted real user data before on another
   project.
6. Show me a short plan in plain English — what you're going to build, what
   you're deliberately NOT going to touch — and wait for me to say "go"
   before writing any code.
7. Build it.
8. Run it on the simulator/emulator yourself and show me it actually working
   (a screenshot or the live preview). Don't tell me something is "done" or
   "fixed" without showing me the proof — a claim on its own isn't evidence.
9. Get an independent AI review before this goes anywhere near being
   finished — and it has to actually try to break what you built, not just
   read the code and say it looks fine. Tell me plainly what it found and
   what you changed because of it. Don't skip this because the change looks
   small — the smallest changes are exactly the ones that have slipped
   through unreviewed before.
10. Once it's reviewed and clean, merge it yourself. Don't hand that back to
    me — I don't do git. Tell me plainly whether it's now actually merged, or
    still sitting on a branch waiting for something.

A few standing rules on top of all that:

- Keep going on your own until the task is genuinely finished. Don't stop and
  check in with me just because a step finished — only stop when you hit a
  real decision that's actually mine to make (not something you could
  reasonably decide yourself).
- When you do bring me a decision, give it to me the same way every time: the
  situation in a sentence, the real options with what each one costs and
  gives me, your own recommendation, and a simple way for me to choose. Never
  just ask "what do you think?" with no options laid out.
- If you park or postpone something at my request, don't just drop it — tell
  me when you'll come back to it, and actually come back to it then without
  me having to remind you.
- At every step, tell me in one or two plain sentences what just happened and
  what happens next — like you're talking to a smart friend who's never
  coded, not a written report. Never assume I know a technical term — explain
  it in the same sentence if you have to use one at all. If you're ever about
  to ask me to do something technical, don't — do it yourself, or tell me
  plainly why you genuinely can't and what my one option is.
```

Once you've pasted that, just talk normally — "add a button that lets people
skip a habit for one day," "the streak counter looks wrong on Android," "I
think onboarding is too long." Claude takes it from there.

---

## What the steps actually look like

You don't need to remember these — the message above makes Claude do them
automatically. This is just so you know what "normal" looks like, and can
tell if something's being skipped.

| # | What happens | What you do |
|---|---|---|
| 1 | Claude repeats back what you asked for | Say "yes" or correct it |
| 2 | Claude pushes back / asks "are you sure?" | Answer honestly — this step is supposed to feel like friction |
| 3 | Claude checks the agreed plan (the handbook) for conflicts | Read what it flags, decide, move on |
| 4 | For anything visual, Claude shows you a picture first | Look at it properly — this is your one real chance to change wording or layout cheaply |
| 5 | For anything touching real user data, Claude names the risk | Ask "what could this wrongly affect?" if it isn't obvious |
| 6 | Claude shows you a short plan before writing anything | Approve it, or say what to change |
| 7 | Claude actually builds it | Nothing — this is Claude's work |
| 8 | Claude runs it on a simulator and shows you it working | Look at it. Does it look and behave right? |
| 9 | A second, independent AI tries to break the work, not just read it | Nothing — this happens automatically |
| 10 | Claude merges the finished, reviewed work itself | Nothing — Claude does this too |

If any of steps 3, 4, 5, 9, or 10 seem to have been skipped, ask directly:
> *"Did you check the handbook for this? Did I see a picture before this got
> built? Did an independent review actually try to break it? Is this
> genuinely merged, or just sitting on a branch?"*

---

## Red flags — stop and ask Salim

You don't need to catch everything technical. But stop and loop in Salim if:

- Claude wants to **release something, submit to an app store, touch money,
  or send a message in the founder's name** — none of that is yours or
  Claude's to approve.
- Claude wants to **build the app onto a real phone** — that always needs
  Salim's go-ahead first.
- Claude says something **needs a secret, a password, or an API key** you
  don't recognise.
- Anything that could **delete, merge, or overwrite a real user's habits,
  streaks, entries, or account** — even if Claude says it's low-risk. This
  gets a second pair of eyes every time, no exceptions, because it's the one
  kind of mistake that can't be undone.
- Claude says it's **blocked or unsure** and asks you a genuinely product-level
  question you can't answer confidently (not "which button colour" — those
  are yours; "should we change how streaks work" — check with Salim).
- Claude says it's **"waiting" on something** without a clear plan to check
  back on its own — ask what it's waiting for, and whether it's going to
  follow up itself or just leave it sitting.

Everything else — building, testing, reviewing, merging finished work — is
Claude's job to just do.

---

## The short version

1. `cd ~/dev/one-percent` → `claude` — same way, every time. One topic, one
   chat.
2. Paste the big instruction block once per new chat.
3. Talk in plain English about what you want.
4. Let Claude push back, check the plan, **show you a picture** of anything
   visual, flag anything touching real user data, show you a plan, build,
   test on the simulator with proof, get a review that actually tries to
   break it, and merge — all before it tells you "done."
5. Never open a code editor. Never run a technical command it hasn't given
   you word-for-word. If it asks you to, tell it to do it itself instead.
