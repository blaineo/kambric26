#!/usr/bin/env python3
"""Batch 20: writes descriptions.csv (the reviewable drafts) from DRAFTS below + before.json.
Multi-print products get "Print | description" (the print part = the current alt, so grouping is unchanged)."""
import csv, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
SV, SC, CV, CO, RN, LI, MV, CT, SK = ("silk viscose slip dress", "silk-cotton voile square scarf", "cotton voile bandana",
    None, "recycled nylon swimsuit", "organic linen sundress", "matte viscose kaftan", "brushed cotton car coat", "silk slip dress")
def m(view, pr, what="recycled nylon swimsuit"): return f"{view}, {pr} {what}"
DRAFTS = {
 "kati-slip-dress-in-matyo-floral": [
  "Front view worn in a field of teasels, Matyó Floral silk viscose slip dress",
  "Back view showing the low V-back, Matyó Floral silk viscose slip dress",
  "Flat product shot of the bias-cut slip dress in Matyó Floral silk viscose",
  "Worn with the Matyó Floral Vera coat over one shoulder, Matyó Floral silk viscose slip dress",
  "Front view against a wooden fence, Matyó Floral silk viscose slip dress",
  "Back view showing the low V-back and spaghetti straps, Matyó Floral silk viscose",
  "Close-up of the scoop neckline and diagonal border stripe, Matyó Floral silk viscose",
  "Close-up of the bias-cut skirt falling to the ankle, Matyó Floral silk viscose"],
 "jessie-slip-dress-in-twilight-plumes": [
  "Front view worn in a sunlit meadow, Twilight Plumes silk viscose slip dress",
  "Back view showing the low back, Twilight Plumes silk viscose slip dress",
  "Flat product shot of the bias-cut slip dress in Twilight Plumes silk viscose",
  "Side view walking through tall grass, Twilight Plumes silk viscose slip dress",
  "Front view with the matching Bodie scarf at the neck, Twilight Plumes silk viscose slip dress"],
 "bodie-scarf-in-twilight-plumes": [
  "Held overhead in the breeze, Twilight Plumes silk-cotton voile square scarf",
  "Worn as a headscarf, seated on a bench, Twilight Plumes silk-cotton voile square scarf",
  "Tied over the hair, Twilight Plumes silk-cotton voile square scarf"],
 "goldie-bandana-in-matyo-floral": [
  "Tied as a headscarf, Matyó Floral cotton voile bandana",
  "Back view tied as a headscarf with a bow at the nape, Matyó Floral cotton voile bandana"],
 "margit-one-piece": [
  m("Front view showing the straight neckline and high French-cut leg", "Dahlia Seed"),
  m("Back view showing the scoop back and adjustable straps", "Dahlia Seed"),
  "Flat product shot of the one-piece swimsuit in Dahlia Seed",
  m("Close-up of the straight neckline and spaghetti straps", "Moon Illusion"),
  m("Back view showing the scoop back", "Moon Illusion"),
  m("Front view showing the high French-cut leg", "Moon Illusion"),
  "Flat product shot of the one-piece swimsuit in Moon Illusion",
  m("Three-quarter back view", "Moon Illusion"),
  m("Front view showing the high French-cut leg", "Good Vibrations"),
  m("Back view showing the scoop back and adjustable straps", "Good Vibrations"),
  "Flat product shot of the one-piece swimsuit in Good Vibrations",
  m("Close-up of the straight neckline and spaghetti straps", "Good Vibrations"),
  m("Close-up of the print and high-cut leg", "Pastel Asterisk"),
  m("Front view showing the straight neckline and high French-cut leg", "Pastel Asterisk"),
  "Flat product shot of the one-piece swimsuit in Pastel Asterisk",
  m("Back view showing the scoop back", "Pastel Asterisk"),
  m("Side view showing the high-cut leg", "Pastel Asterisk"),
  m("Close-up of the bodice and print", "Orange Asterisk"),
  m("Front view showing the high French-cut leg", "Orange Asterisk"),
  m("Close-up of the straight neckline and spaghetti straps", "Orange Asterisk"),
  "Flat product shot of the one-piece swimsuit in Orange Asterisk",
  m("Back view showing the scoop back and adjustable straps", "Orange Asterisk"),
  m("Close-up of the bodice and high-cut leg", "Magnolia"),
  m("Front view showing the straight neckline and high French-cut leg", "Magnolia"),
  "Flat product shot of the one-piece swimsuit in Magnolia",
  m("Worn at the beach carrying a surfboard", "Magnolia"),
  m("Worn with jeans beside a surfboard", "Magnolia"),
  m("Front view by a sunny window", "Matyó Floral"),
  m("Shown on a dress form", "Matyó Floral"),
  m("Back view by a sunny window", "Matyó Floral"),
  m("Worn seated on a wooden floor", "Wildflowers"),
  "Flat product shot of the one-piece swimsuit in Wildflowers, showing the pink lining",
  m("Back view seated on a wooden floor", "Wildflowers")],
 "zadie-linen-dress": [
  m("Front view showing the V-neckline", "Wildflowers", LI),
  m("Back view showing the crossed tie-back straps", "Wildflowers", LI),
  m("Close-up of the crossed straps tied at the back", "Wildflowers", LI),
  m("Side view of the open back and tie straps", "Wildflowers", LI),
  "Flat product shot of the sundress in Wildflowers organic linen",
  m("Full-length front view", "Candied Plaid", LI),
  m("Seated in a folding lawn chair", "Candied Plaid", LI),
  "Flat product shot of the sundress in Candied Plaid organic linen",
  m("Back view showing the crossed tie-back straps", "Candied Plaid", LI),
  m("Close-up of the V-neckline and bias-cut plaid", "Candied Plaid", LI),
  m("Front view showing the V-neckline", "Cherry Coupe", LI),
  m("Full-length front view", "Cherry Coupe", LI),
  m("Back view showing the crossed tie-back straps", "Cherry Coupe", LI),
  "Flat product shot of the sundress in Cherry Coupe organic linen"],
 "esther-kaftan": [
  m("Back view showing the butterfly sleeves and side slit", "Good Vibrations", MV),
  m("Close-up of the deep V-neck and waist sash", "Good Vibrations", MV),
  m("Front view with the sash tied at the waist", "Good Vibrations", MV),
  m("Side view mid-stride showing the side slit", "Good Vibrations", MV),
  m("Front view worn loose in a wood-panelled hallway", "Dahlia Seed", MV),
  m("Side view showing the wide butterfly sleeve", "Dahlia Seed", MV),
  m("Close-up of the sleeve and its pink lining", "Dahlia Seed", MV),
  m("Front view showing the deep V-neck and butterfly sleeves", "Dahlia Seed", MV),
  m("Full-length view showing the pink sleeve lining", "Dahlia Seed", MV),
  m("Side view of the floor-length hem", "Dahlia Seed", MV),
  m("Close-up of the deep V-neck and sleeve lining", "Magnolia", MV),
  m("Close-up of the V-neck and waist sash", "Magnolia", MV),
  m("Full-length front view with the sash tied at the waist", "Magnolia", MV),
  m("Back view showing the sash tied at the back and the side slit", "Magnolia", MV),
  m("Close-up of the sleeve and its ivory lining", "Magnolia", MV),
  m("Worn in the sun against a teal wall", "Magnolia", MV),
  m("Worn beside a model in a solid ivory kaftan", "Magnolia", MV)],
 "vera-car-coat": [
  m("Back view showing the dropped shoulders, in a meadow", "Midnight Plumes", CT),
  m("Side view in a field of teasels", "Midnight Plumes", CT),
  m("Flat product shot showing the shawl collar and single-button closure", "Midnight Plumes", CT),
  m("Walking through a meadow, hand in the slash pocket", "Midnight Plumes", CT),
  m("Full-length view in a meadow", "Midnight Plumes", CT),
  m("Worn open over a matching slip dress among teasels", "Matyó Floral", CT),
  m("Holding the shawl collar among teasels", "Matyó Floral", CT),
  m("Flat product shot showing the shawl collar and single-button closure", "Matyó Floral", CT),
  m("Back view showing the Western-style back yoke", "Matyó Floral", CT),
  m("Front view worn open with the cuffs turned back", "Matyó Floral", CT)],
 "arielle-dress": [
  "Worn in a field of teasels, Parlor Rose silk slip dress in Olive",
  "Three-quarter front view, Parlor Rose silk slip dress in Olive",
  "Front view showing the squared neckline, Parlor Rose silk slip dress in Olive",
  "Back view showing the low V-back, Parlor Rose silk slip dress in Olive",
  "Detail of the Parlor Rose print in Olive: cream roses between vine borders",
  "Back view in a field of teasels showing the low V-back, Parlor Rose silk slip dress in Terracotta",
  "Three-quarter view showing the squared neckline, Parlor Rose silk slip dress in Terracotta",
  "Full-length front view, Parlor Rose silk slip dress in Terracotta",
  "Back view showing the low V-back, Parlor Rose silk slip dress in Terracotta",
  "Detail of the Parlor Rose print in Terracotta: tonal roses between vine borders"],
}
B = json.load(open(os.path.join(HERE, "before.json")))
rows = []
for p in B["products"]["nodes"]:
    media = [x for x in p["media"]["nodes"] if x.get("image")]
    if not media: continue
    d = DRAFTS[p["handle"]]; assert len(d) == len(media), (p["handle"], len(d), len(media))
    prints = {v for o in p["options"] if o["name"] in ("Print", "Colorway") for v in o["values"]}
    for n, (x, desc) in enumerate(zip(media, d), 1):
        cur = x["alt"] or ""
        if cur in prints: assert cur.lower() in desc.lower(), (p["handle"], n, cur, desc)
        new = f"{cur} | {desc}" if cur in prints else desc
        assert len(new) <= 512
        rows.append({"handle": p["handle"], "n": n, "media_id": x["id"], "file": x["image"]["url"].split("/")[-1].split("?")[0],
                     "current_alt": cur, "new_alt": new})
with open(os.path.join(HERE, "descriptions.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(len(rows), "rows; longest", max(len(r["new_alt"]) for r in rows), "chars")
