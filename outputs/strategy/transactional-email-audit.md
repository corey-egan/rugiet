# Transactional Email Audit: One-Click Unsubscribe & Sending Domain

**Date:** 2026-06-13
**Source:** Braze canvas/details API (all active canvases)
**Scope:** 111 canvases audited across 4 parallel batches

---

## Executive Summary

**97 transactional email steps** were found across **73 canvases**, all sending from `notifications@notifications.rugiet.com`. **Every single one has `headers: null`** — meaning no one-click unsubscribe (List-Unsubscribe / List-Unsubscribe-Post) header is configured at the individual message level.

---

## Finding: No One-Click Unsubscribe on Any Transactional Step

| Metric | Value |
|---|---|
| Total canvases audited | 111 |
| Canvases with transactional steps | 73 |
| Total transactional email steps | 97 |
| Steps with `headers: null` | **97 (100%)** |
| Steps with one-click unsubscribe configured | **0** |

All transactional steps use:
- **From:** `RUGIET <notifications@notifications.rugiet.com>`
- **Reply-to:** `customercare@rugiet.com`
- **Footer:** `Rugiet_Footer_2026_Transactional` content block (with 3 exceptions noted below)

---

## Full Inventory of Transactional Steps

### Order Confirmation (7 steps)

| Canvas | Canvas ID | Step Name | Step ID | Subject | Headers |
|---|---|---|---|---|---|
| Ready Order Confirmation | `d2417f1d` | `_ready_lead_auto_tx_email_0_order-confirmation` | `99288034` | Order confirmed | `null` |
| Go Long Order Confirmation | `d10873a0` | `_go-long_lead_auto_tx_email_0_order-confirmation` | `14ddebf0` | Your order is confirmed | `null` |
| Boost Order Confirmation | `aa867bc9` | `_boost_lead_auto_tx_email_0_order-confirmation` | `5ee8376a` | Your order is confirmed | `null` |
| Grower Order Confirmation | `e981430a` | `_grower_lead_auto_tx_email_0_order-confirmation` | `1d625e78` | Your order is confirmed | `null` |
| Weigh In Order Confirmation | `3a974cd6` | `_weigh-in_lead_auto_tx_email_0_order-confirmation` | `c6baaa7e` | Your order is confirmed | `null` |
| Recharge Order Confirmation | `d0efdf48` | `_recharge_lead_auto_tx_email_0_order-confirmation` | `a1e00b36` | Your order is confirmed | `null` |
| Longevity Order Confirmation | `75f4c0d8` | `_longevity_lead_auto_tx_email_0_order-confirmation` | `55e43fcb` | Your order is confirmed | `null` |

### Prescription Approved (9 steps)

| Canvas | Canvas ID | Step Name | Step ID | Subject | Headers |
|---|---|---|---|---|---|
| Ready Prescribed | `95699f47` | `_ready_lead_auto_tx_email_0_approved` | `9207055d` | Your prescription is approved | `null` |
| Go Long Prescribed | `ac6b2b71` | `_go-long_lead_auto_tx_email_0_approved` | `d2bc81c8` | Your prescription is approved | `null` |
| Boost Prescribed | `6baab8fd` | `_boost_active_auto_tx_email_0_approved` | `190f01e3` | Your prescription is approved | `null` |
| Grower Prescribed | `30e0fdbe` | `_grower_active_auto_tx_email_0_approved` | `b6625064` | Your prescription is approved | `null` |
| Weigh In Prescribed | `b96d8c5d` | `_weigh-in_active_auto_tx_email_0_approved` | `5cc61b4d` | Your prescription is approved | `null` |
| Recharge Prescribed | `5e10389c` | `_recharge_active_auto_tx_email_0_approved` | `eacb3a40` | Your prescription is approved | `null` |
| Longevity Prescribed | `dac71394` | `_longevity_active_auto_tx_email_0_approved` | `a12d1e0d` | Your prescription is approved | `null` |
| TRT Prescribed (Injectable) | `6f7abf73` | `_trt_active_auto_tx_email_0_approved` | `34239e78` | Time to restore what's missing | `null` |
| TRT Prescribed (Topical) | `6f7abf73` | `_trt_active_auto_tx_email_0_approved_topical` | `96d99e4e` | Time to restore what's missing | `null` |

### Shipped (8 steps)

| Canvas | Canvas ID | Step Name | Step ID | Subject | Headers |
|---|---|---|---|---|---|
| Ready Shipped | `04db07ab` | `_ready_active_auto_tx_email_0_shipped` | `fd96c80a` | Your Ready shipment is on its way | `null` |
| Go Long Shipped | `f9385489` | `_go-long_active_auto_tx_email_0_shipped` | `55e63b2a` | Your order has shipped | `null` |
| Boost Shipped | `8491bd26` | `_boost_active_auto_tx_email_0_shipped` | `1b2ddec6` | Your order has shipped | `null` |
| Grower Shipped | `94d415bb` | `_grower_active_auto_tx_email_0_shipped` | `afbc4d88` | Your order has shipped | `null` |
| Weigh In Shipped | `dcd163fc` | `_weigh-in_active_auto_tx_email_0_shipped` | `ec2dd19b` | Your order has shipped | `null` |
| Recharge Shipped | `b09c13d7` | `_recharge_active_auto_tx_email_0_shipped` | `28382b44` | Your order has shipped | `null` |
| Longevity Shipped | `5d5eacaf` | `_longevity_active_auto_tx_email_0_shipped` | `b9ff3d5c` | Your order has shipped | `null` |
| TRT Shipped | `5a6d9029` | `_trt_active_auto_tx_email_0_shipped` | `61dca1b2` | Your order has shipped | `null` |

### Order Delivered (2 steps)

| Canvas | Canvas ID | Step Name | Step ID | Subject | Headers |
|---|---|---|---|---|---|
| Ready - Order Delivered | `5c4f4c1b` | `_ready_active_auto_tx_email_0_delivered` | `48a31490` | Your Ready order has arrived | `null` |
| Longevity Order Delivered | `c88d7a73` | `_longevity_active_auto_tx_email_0_delivered` | `086e203a` | Your treatment has arrived | `null` |

### Refill Processed (7 steps)

| Canvas | Canvas ID | Step Name | Step ID | Subject | Headers |
|---|---|---|---|---|---|
| Ready - Refill Processed | `e6619520` | `_ready_active_auto_tx_email_0_refill-processed` | `dba442b0` | Your refill is coming | `null` |
| Go Long - Refill Processed | `7d0538a3` | `_go-long_active_auto_tx_email_0_refill-processed` | `06aa549b` | Your refill is coming | `null` |
| Boost - Refill Processed | `abae2aee` | `_boost_active_auto_tx_email_0_refill-processed` | `b5522b96` | Your refill is coming | `null` |
| Grower - Refill Processed | `207d4a9d` | `_grower_active_auto_tx_email_0_refill-processed` | `daaf4dc8` | Your refill is coming | `null` |
| Weigh In - Refill Processed | `3657d732` | `_weigh-in_active_auto_tx_email_0_refill-processed` | `2fcd87db` | Your refill is coming | `null` |
| Recharge - Refill Processed | `0e55547e` | `_recharge_active_auto_tx_email_0_refill-processed` | `881c6486` | Your refill is coming | `null` |
| Longevity Refill Processed | `4b08dc7f` | `_longevity_active_auto_tx_email_0_refill-processed` | `6fb8e5d0` | Your refill is processing | `null` |

### Refill Reminder (10 steps)

| Canvas | Canvas ID | Step Name | Step ID | Subject | Headers |
|---|---|---|---|---|---|
| Ready Refill Reminder | `8017501b` | `_ready_active_auto_tx_email_0_upcoming-refill` | `001a3f05` | Confidence, delivered. | `null` |
| Go Long Refill Reminder | `91d7d3c4` | `_go-long_active_auto_tx_email_0_upcoming-refill` | `cfa25236` | Your Go Long will keep going | `null` |
| Boost Refill Reminder | `5e181059` | `_boost_active_auto_tx_email_0_upcoming-refill` | `7d7dfbff` | Refill Reminder | `null` |
| Grower Refill Reminder | `fccf74c5` | `_grower_active_auto_tx_email_0_upcoming-refill` | `a9be6843` | Refill Reminder | `null` |
| Weigh In Refill Reminder | `171eb081` | `_weigh-in_active_auto_tx_email_0_upcoming-refill` | `9653f880` | Refill Reminder | `null` |
| Recharge Refill Reminder | `2288b385` | `_recharge_active_auto_tx_email_0_upcoming-refill` | `d60328d6` | Refill Reminder | `null` |
| Longevity Refill Reminder | `4559235d` | `_longevity_active_auto_tx_email_0_upcoming-refill` | `3e93f385` | Refill Reminder | `null` |
| TRT Refill Reminder (Injectable) | `299dc490` | `_trt_active_auto_tx_email_0_upcoming-refill` | `e60f6511` | Refill Reminder | `null` |
| TRT Refill Reminder (Enclomiphene) | `299dc490` | `_trt-enclo_active_auto_tx_email_0_upcoming-refill` | `9a890138` | Refill Reminder | `null` |
| TRT Refill Reminder (Incomplete Check-in) | `299dc490` | `_trt_active_auto_tx_email_0_upcoming-refill-incomplete-checkin` | `f1e4a79e` | Your next charge will process in 7 days | `null` |

### Payment Failed (6 steps)

| Canvas | Canvas ID | Step Name | Step ID | Subject | Headers |
|---|---|---|---|---|---|
| Ready Payment Failed | `e82c2d6b` | `_ready_all_auto_tx_email_0_payment-failed` | `89566abe` | We couldn't process your payment | `null` |
| Go Long Payment Failed | `494cdd94` | `_go-long_all_auto_tx_email_0_payment-failed` | `43c5a06b` | We couldn't process your payment | `null` |
| Boost Payment Failed | `8173dd88` | `_boost_all_auto_tx_email_0_payment-failed` | `b9203eaa` | We couldn't process your payment | `null` |
| Grower Payment Failed | `7057bc97` | `_grower_all_auto_tx_email_0_payment-failed` | `126e1ccf` | We couldn't process your payment | `null` |
| Weigh In Payment Failed | `420933e3` | `_weigh-in_all_auto_tx_email_0_payment-failed` | `0b53a0a5` | We couldn't process your payment | `null` |
| Recharge Payment Failed | `b64188db` | `_recharge_all_auto_tx_email_0_payment-failed` | `f6202be7` | We couldn't process your payment | `null` |

### Cancelled Membership (10 steps across 5 canvases)

| Canvas | Canvas ID | Step Name | Step ID | Subject | Headers |
|---|---|---|---|---|---|
| Ready Cancelled Membership | `22b031de` | `_ready_inactive_auto_tx_email_0_cancelled` | `8c16974c` | Your Account Update | `null` |
| Ready Cancelled Membership | `22b031de` | `_ready_inactive_auto_tx_email_0_cancelled_failed-payment` | `02d43c67` | Your Subscription Has Been Cancelled | `null` |
| Boost Cancelled Membership | `97b0b566` | `_boost_inactive_auto_tx_email_0_cancelled` | `a17e0d89` | Your Account Update | `null` |
| Boost Cancelled Membership | `97b0b566` | `_boost_inactive_auto_tx_email_0_cancelled_failed-payment` | `16479989` | Your Subscription Has Been Cancelled | `null` |
| Weigh In Cancelled Membership | `5de841b7` | `_weigh-in_inactive_auto_tx_email_0_cancelled` | `f103e7f9` | Your Account Update | `null` |
| Weigh In Cancelled Membership | `5de841b7` | `_weigh-in_inactive_auto_tx_email_0_cancelled_failed-payment` | `30c0d045` | Your Subscription Has Been Cancelled | `null` |
| Grower Cancelled Membership | `d6ed96db` | `_grower_inactive_auto_tx_email_0_cancelled` | `ea894ab8` | Your Account Update | `null` |
| Grower Cancelled Membership | `d6ed96db` | `_grower_inactive_auto_tx_email_0_cancelled_failed-payment` | `81507ca7` | Your Subscription Has Been Cancelled | `null` |
| Recharge Cancelled Membership | `884ac80d` | `_recharge_inactive_auto_tx_email_0_cancelled` | `eca1c923` | Your Account Update | `null` |
| Recharge Cancelled Membership | `884ac80d` | `_recharge_inactive_auto_tx_email_0_cancelled_failed-payment` | `26b4156b` | Your Subscription Has Been Cancelled | `null` |

### Longevity Cancelled Membership (2 steps)

| Canvas | Canvas ID | Step Name | Step ID | Subject | Headers |
|---|---|---|---|---|---|
| Longevity Cancelled Membership | `4ff67d96` | `_longevity_inactive_auto_tx_email_0_cancelled` | `3951c2b4` | Your Account Update | `null` |
| Longevity Cancelled Membership | `4ff67d96` | `_longevity_inactive_auto_tx_email_0_cancelled_failed-payment` | `bdc19e8c` | Your Subscription Has Been Cancelled | `null` |

### Prescription Expired (8 steps)

| Canvas | Canvas ID | Step Name | Step ID | Subject | Headers |
|---|---|---|---|---|---|
| Ready Prescription Expired | `aff6234f` | `_ready_expired_auto_tx_email_0_expired` | `63ca8c0d` | You're about to run out, a prescription renewal is required | `null` |
| Go Long Prescription Expired | `3efe3f4b` | `_go-long_expired_auto_tx_email_0_expired` | `120b12d3` | You're about to run out, a prescription renewal is required | `null` |
| Boost Prescription Expired | `73be5e2d` | `_boost_expired_auto_tx_email_0_expired` | `740f987a` | You're about to run out, a prescription renewal is required | `null` |
| Grower Prescription Expired (new) | `875cf066` | `_grower_expired_auto_tx_email_0_expired` | `3b8befec` | You're about to run out, a prescription renewal is required | `null` |
| Grower Prescription Expired (old) | `aba0daaa` | `_grower_expired_auto_tx_email_0_expired` | `21024dab` | You're about to run out, a prescription renewal is required | `null` |
| Weigh In Prescription Expired | `b0db3b28` | `_weigh-in_expired_auto_tx_email_0_expired` | `d9181b78` | You're about to run out, a prescription renewal is required | `null` |
| Recharge Prescription Expired (new) | `ee75024c` | `_recharge_expired_auto_tx_email_0_expired` | `f0c799df` | You're about to run out, a prescription renewal is required | `null` |
| Longevity Prescription Expired | `c6eaf1a0` | `_longevity_expired_auto_tx_email_0_expired` | `33677d50` | You're about to run out, a prescription renewal is required | `null` |

### ID Verification (6 steps)

| Canvas | Canvas ID | Step Name | Step ID | Subject | Headers |
|---|---|---|---|---|---|
| Ready - ID Incomplete | `b1bb9207` | `_ready_lead_auto_tx_email_0_id-verification` | `ef42a66e` | Action Required: ID Verification | `null` |
| Go Long - ID Incomplete | `37adef09` | `_go-long_lead_auto_tx_email_0_id-verification` | `7f23ac3c` | Action Required: ID Verification | `null` |
| Boost - ID Incomplete | `fd41a7e9` | `_boost_lead_auto_tx_email_0_id-verification` | `1643abd4` | Action Required: ID Verification | `null` |
| Grower - ID Incomplete | `aa60be74` | `_grower_lead_auto_tx_email_0_id-verification` | `81ad8578` | Action Required: ID Verification | `null` |
| Weigh In - ID Incomplete | `6a4b6a8a` | `_weigh-in_lead_auto_tx_email_0_id-verification` | `3cb60d0a` | Action Required: ID Verification | `null` |
| Recharge - ID Incomplete | `748a5958` | `_recharge_lead_auto_tx_email_0_id-verification` | `87e709e0` | Action Required: ID Verification | `null` |

### Synchronous Care / TRT Appointments (4 steps)

| Canvas | Canvas ID | Step Name | Step ID | Subject | Headers |
|---|---|---|---|---|---|
| Synchronous Care Initial Scheduling | `90a05245` | `_any_active_auto_tx_email_0_synchronous-care` | `b30e48ea` | Action Required: Schedule Your Appointment | `null` |
| TRT - Sync Required (initial) step A | `b84bfc87` | `_trt_lead_auto_tx_email_0_synchronous-care_initial-schedule` | `1e052ab7` | You're ready to schedule your appointment | `null` |
| TRT - Sync Required (initial) step B | `b84bfc87` | `_trt_lead_auto_tx_email_1_synchronous-care_initial-schedule` | `7a8b9726` | You're ready to schedule your appointment | `null` |
| TRT Synchronous Visit Scheduled | `0d87b1c9` | `_trt_inactive_auto_tx_email_0_synchronous-care_scheduled` | `3714dcfe` | See you soon: your appointment details | `null` |
| TRT - Sync Appointment 15 mins | `79c08b27` | (unnamed step) | `4eddf6d6` | Reminder: your appointment is coming up | `null` |

### Labs (14 steps across 3 canvases)

| Canvas | Canvas ID | Step Name | Step ID | Subject | Headers |
|---|---|---|---|---|---|
| Labs Complete (step A) | `09b774ce` | `_labs_lead_auto_tx_email_0_labs-complete` | `d39a2c08` | Your lab results are in | `null` |
| Labs Complete (step B) | `09b774ce` | `_labs_lead_auto_tx_email_0_labs-complete` | `fff9d60c` | Your consultation is waiting | `null` |
| Labs Order Confirmation - At Home (6 steps) | `09d089a4` | `_tx_email_0` through `_tx_email_5_order-confirmation_at-home` | various | Your lab order is confirmed → escalating reminders | `null` |
| Labs Order Confirmation - In Office (6 steps) | `26f1ed7c` | `_tx_email_0` through `_tx_email_5_order-confirmation_in-office` | various | Your lab order is confirmed → escalating reminders | `null` |

### Misc: Transactional Domain with Marketing Footer (1 step — anomaly)

| Canvas | Canvas ID | Step Name | Step ID | Subject | Headers | Note |
|---|---|---|---|---|---|---|
| Go Long - ID Incomplete | `37adef09` | `_go-long_lead_auto_mk_email_2_id-verification` | `504e70b8` | Action Required: ID Verification | `null` | Sends from tx domain but uses marketing footer (`Rugiet_Footer_2026`) |

---

## Anomalies & Footer Exceptions

| Canvas | Step ID | Issue |
|---|---|---|
| **Ready Prescribed** (`95699f47`) | `9207055d` | Uses image-based footer instead of `Rugiet_Footer_2026_Transactional` content block |
| **Recharge Prescription Expired** (`a1a578dc`) | `7c031799` | Uses image-based footer with inline unsubscribe link (older template) |
| **Go Long - ID Incomplete** (`37adef09`) | `504e70b8` | Step name says `_mk_` (marketing) but sends from `notifications.rugiet.com` — uses marketing footer |

---

## Implications

1. **One-click unsubscribe is not configured on any transactional email at the message level.** The `headers` field is `null` across all 97 steps. Whether one-click unsubscribe is applied depends on Braze workspace-level email settings and sending domain configuration — these are not visible via the canvas/details API.

2. **If Braze workspace settings auto-apply List-Unsubscribe to all emails (including transactional),** that could be problematic — patients could inadvertently unsubscribe from critical payment, shipping, and prescription communications.

3. **If workspace settings do NOT auto-apply one-click unsubscribe to the notifications.rugiet.com sending domain,** then these transactional emails are compliant — truly transactional messages (order confirmations, shipping, payment failures) are exempt from CAN-SPAM unsubscribe requirements.

4. **The 3 footer anomalies should be standardized** to use the `Rugiet_Footer_2026_Transactional` content block for consistency.
