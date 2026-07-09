# Care Pair Templates — NAD+ Cross-Sell

**Date:** 2026-06-17
**Owner:** Lifecycle
**Status:** Draft for team review
**Trigger:** Patient prescribed NAD+ (prescription approved)
**Channel:** Care Pair (provider-to-patient in-app message)

---

## Context

These are Care Pair message templates sent from the approving provider after a patient is prescribed NAD+. Each message recommends one or both longevity add-ons based on the patient's likely goals. The provider's name and credentials auto-populate via Care Pair.

**Cross-sell products:**
- **Sermorelin** — growth hormone peptide. Best positioned for patients who are actively training or serious about physical performance. Not a blanket recommendation.
- **Glutathione** — master antioxidant. Positioned around detox, immune support, and recovery. Broader applicability.

**Tone:** Provider voice — warm, direct, clinically grounded. These should read like a real message from a doctor who knows the patient's case, not marketing copy. Rugiet-branded but provider-first.

**Length target:** ~70–100 words per message (benchmarked against existing provider template).

---

## A. Sermorelin only

Sermorelin is qualified — the recommendation acknowledges it's most relevant for patients who are actively working out or focused on physical performance.

---

### A1

Hi [patient_name], I've approved your NAD+ treatment and wanted to flag something else that may be relevant depending on your routine. If you're someone who trains regularly or is serious about gym time, sermorelin can help support recovery, lean muscle, and sleep quality — benefits that tend to compound with what NAD+ is already doing at the cellular level. If that sounds like your situation, you can learn more here: [sermorelin product link]

---

### A2

Hi [patient_name], your NAD+ prescription is approved and on its way. I also wanted to mention sermorelin — a growth hormone peptide that many of my patients who are active in the gym pair with NAD+. It can help support recovery, body composition, and deeper sleep. It's not for everyone, but if physical performance is a priority for you, it's worth a look: [sermorelin product link]

---

### A3

Hi [patient_name], I just approved your NAD+ protocol. One thing I like to share with patients who are consistent with their training — sermorelin can be a strong complement. It supports growth hormone levels, which can help with recovery, lean body composition, and sleep. If you're putting in the work at the gym, this is designed to help you get more out of it. More details here: [sermorelin product link]

---

## B. Glutathione only

Glutathione is a broader recommendation — relevant to any NAD+ patient interested in detox, immune function, or overall cellular protection.

---

### B1

Hi [patient_name], your NAD+ prescription has been approved. I also wanted to mention glutathione — it's the body's primary antioxidant, and it plays a key role in detox and immune support. Many patients on NAD+ add glutathione because the two work on complementary pathways: NAD+ supports cellular energy and repair, while glutathione helps protect those same cells from oxidative stress. If you're interested: [glutathione product link]

---

### B2

Hi [patient_name], I've approved your NAD+ treatment and wanted to share one more option worth considering. Glutathione is something I recommend to patients who are focused on immunity and detox alongside their longevity protocol. It can help support your body's natural defense against oxidative damage — which pairs well with what NAD+ does for cellular energy and repair. You can learn more here: [glutathione product link]

---

### B3

Hi [patient_name], your NAD+ protocol is set. While I have your attention — glutathione is another treatment we offer that complements NAD+ well. NAD+ focuses on energy production and DNA repair at the cellular level. Glutathione handles the other side: protecting cells from the oxidative stress that accelerates aging. If immune support and detox are on your radar, it's worth a look: [glutathione product link]

---

## C. Both — framed around patient goals

These templates recommend both sermorelin and glutathione, but frame the recommendation around the patient's priorities rather than a blanket "add both." Per GTM guidance: sermorelin for patients serious about training, glutathione for detox and immunity.

---

### C1

Hi [patient_name], I've approved your NAD+ prescription and wanted to share two other treatments that pair well with it — depending on your goals. If you're serious about your time in the gym, sermorelin can help support recovery, lean muscle, and sleep quality. If you're more focused on detox and immune health, glutathione is the body's primary antioxidant and works on complementary pathways to NAD+. Take a look and see which fits where you are right now:

Sermorelin: [sermorelin product link]
Glutathione: [glutathione product link]

---

### C2

Hi [patient_name], your NAD+ treatment is approved. I like to let patients know about two options that can complement what NAD+ does, depending on what matters most to you. For patients who are active and training consistently, sermorelin supports growth hormone levels — which can help with recovery and body composition. For patients focused on immunity and cellular protection, glutathione helps defend against the oxidative stress that accelerates aging. Both work well alongside NAD+, but the right fit depends on your priorities:

Sermorelin: [sermorelin product link]
Glutathione: [glutathione product link]

---

### C3

Hi [patient_name], I just approved your NAD+ protocol. Two other treatments are worth knowing about as you build out your longevity plan. Sermorelin is a growth hormone peptide — best suited for men who are putting in real work at the gym and want to support recovery and sleep. Glutathione is the body's master antioxidant — more relevant if detox and immune support are priorities for you. No pressure on either, but both complement NAD+ well:

Sermorelin: [sermorelin product link]
Glutathione: [glutathione product link]

---

## Compliance check

- [x] Conditional verbs on all benefit claims ("can help," "supports," "designed to," "tends to")
- [x] No guarantees or absolute outcome promises
- [x] Optimization register — framing upgrade and capability, not deficiency
- [x] No exclamation points
- [x] Sermorelin qualified with training/gym context (per GTM guidance)
- [x] No fabricated doctor quotes — these are templates for actual providers to send
- [x] No disease treatment claims
- [x] Product links direct to Rugiet product pages (no off-platform claims)

---

## Notes for review

1. **Personalization variable:** All templates use `[patient_name]` — confirm this matches Care Pair's merge tag syntax.
2. **Link format:** Templates use `[product link]` placeholders. Confirm whether Care Pair supports hyperlinked text or requires raw URLs.
3. **Provider attribution:** These templates assume the provider's name and credentials auto-populate. Confirm how Care Pair handles sender identity.
4. **Sermorelin qualifying language:** GTM flagged that sermorelin isn't a fit for everyone — all A and C templates include a fitness/gym qualifier. If the team wants a version without the qualifier, flag it and we'll draft alternatives.
5. **Character limits:** If Care Pair has a message length cap, let us know and we'll trim accordingly. Current templates range from ~75 to ~110 words.
