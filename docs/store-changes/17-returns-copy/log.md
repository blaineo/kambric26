# Batch 17 log: Returns page, who pays return shipping ✅ (2026-09-30)

- **Approved:** owner ("approve batch 17"), after confirming: Kambric provides the return label; return shipping is deducted from the refund.
- **Applied:** 2026-09-30T15:47:54Z, `pageUpdate` on `returns`: "Get in touch with your order number and we'll email you a return label and simple instructions." + "Return shipping is deducted from your refund." Previous body in `before.json`.
- **Matches:** theme setting *Who pays for returns* = Customer pays return shipping → `returnFees: ReturnFeesCustomerResponsibility` in product structured data.
- **Verified live** on /pages/returns.
- **Rollback:** `python3 rollback.py`.
