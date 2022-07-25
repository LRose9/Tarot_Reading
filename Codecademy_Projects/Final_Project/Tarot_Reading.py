import random


number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
archetype = ["The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor", "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit", "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance", "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World"]

# Create class for Major Arcana of Deck
class Major:
  def __init__(self, number, archetype, reverse = False):
    self.number = number
    self.archetype = archetype
    self.reverse = reverse

  def __repr__(self):
    return "Card {number} in the Major Arcana of the Tarot, also known as {archetype}".format(number = self.number, archetype = self.archetype)

  def get_attributes(self):
    attributes = [["new beginnings", "Innocence", "a fresh start"], ["transmission of energy", "manipulation", "trickery"], ["deep understanding", "innate knowledge", "authenticity"], ["motherhood", "sensuality", "creative expansion"], ["fatherhood", "authority", "order"], ["dogma", "observation", "societal expectations"], ["courtship", "romance", "excitement"], ["control", "planning", "speed"], ["fortitude", "health", "potency"], ["solitude", "trancendence", "contemplation"], ["change of luck", "revolution", "calendar time"], ["truth", "litigation", "work"], ["sacrifice", "visions", "alertness"], ["regeneration", "entropy", "mortality"], ["equilibrium", "complexity", "refinement"], ["darkness", "indulgence", "abuse"], ["disruption", "shock", "collapse"], ["hope", "beauty", "flow"], ["strangeness", "emergence", "oddity"], ["freedom", "safety", "manifestation"], ["evolution", "internal change", "transformation"], ["timelessness", "integration", "completion"]]
    card_attributes = attributes[self.number]
    return "The energies represented by this card are: " + str(card_attributes[0]) + ", " + str(card_attributes[1]) + " and " + str(card_attributes[2])

number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
rank = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Page", "Knight", "Queen", "King"]
suit = ["Swords", "Pentacles", "Cups", "Wands"]

# Create class for Minor Arcana of Deck:
class Minor:
  def __init__(self, number, rank, suit):
    self.number = number
    self.rank = rank
    self.suit = suit

  def __repr__(self):
    return "The {rank} of {suit} in the minor arcana of the Tarot".format(rank = self.rank, suit = self.suit)

  def get_attributes(self):
    cups_attributes = ["an opening of the heart and soul, generosity and forgiveness", "finding your soul's reflection in another, partnership and celebration of the heart", "friendship and sharing your joy with others, pleasure and companionship", "expand your vision beyond boredom and indifference, what you are seeking is seeking you", "addiction to people and habits, make the choice to move through melancholia and gloom", "pleasure in giving yourself freely to others, a pleasant walk down memory lane", "inspiration through imagination, conjure your fantasies", "question your motives whilst remaining true to yourself, release what is no longer needed", "be careful what you wish for, it is coming to you", "bliss in all areas of life, simple pleasures and happy endings", "unique psychic insight, unbound to the opinions of others", "romantic seduction and flattery, messages are on the way, be patient", "deep compassion for all sentient life, radical insight", "artistic accomplishment and the ability to maintain balance in choppy waters"]
    wands_attributes = ["a spark of passion or insight to be acted upon, insight with transformative power", "partnerships and plotting of ideas, all possibility spread before you", "sharing your vision with the world, expansion of business adventure", "celebration of early success, temper work with play and pleasure", "drama and conflict within a group, warning to keep your wits about you", "taking a moment to celebrate oneself, success with more to come", "a state of internal defensiveness, call to examine your actions", "pure action in motion with no turning back, final destination unknown", "payoff on invested time and energy, a new world opening itself to you", "the end of a cycle of an incredible expenditure of resources, no more effort is required", "a hint of what is possible when remembering what used to excite you, return to childlike imagination", "feeling the call to share perspective, ignition of energy required for great feats", "dazzeling presence and charisma, control and wisdom in the channelling of energies", "power and presence commanding attention and notoriety, adaptability without compromise"]
    swords_attributes = ["clear articulate thoughts, calling out what is and standing for others", "moving inward to reassess thoughts and feelings, arriving at your own answer without external influence", "a breaking open of the heart in response to extreme pain or transcendence, discomfort from personal growth", "respite of the mind, intellectual stability and preparation for things to come", "disputes involving taking advantage of another, cruelty and unfair advantage", "passage into a better phase of life, showing others the way to freedom", "sneaking away with the spoils while others are distracted, taking only what you need and keep future plans to yourself", "feeling stifled, desperation for an answer yet inability to find one", "nightmares and mental anguish, dark thoughts and a restless mind","the complete and final end of a situation, release and departure", "wisdom and insight, allowing others to underestimate you to obtain the upper hand", "reaching hasty conclusions that may not be based in truth, rushing into a situation compulsively", "wisdom imparted with kindness and precision, honesty without cruelty", "understanding the impact of thoughts and ideas on the world, harnessing gifts to fix what is broken"]
    pentacles_attributes = ["holding the world in the palm of your hand, gifts and money from an unexpected place", "a weighing of two fruitful choices, excitement and performance", "construction and collaboration, surround yourself with expertise and allow yourself to be inspired", "solid foundations leading to future growth, plan ahead but remain flexible", "a dark night of the soul, seek help to overcome adversity", "a balance of give and take, the ability to recieve as easily as you give", "development culminating in the need for reassessment, carefully consider the next step", "utilizing the gifts and talents of your soul, show up and do the work knowing the payoff is worth it", "pleasure in luxurious solitude, the cultivation of your truest self", "having it all only to realize none of it matters, transcending the material", "the quest for knowledge and understanding, learning with the entirety of your being", "waitng for the right moment to present itself, then thoroughly enjoying it", "pleasure in domestic endeavors, nurturing others through creature comforts", "a financial success story, long term investments building wealth and prosperity"]
    if self.suit == "Cups":
      attribute = cups_attributes[self.number]
      return "The suit of Cups reflects elemental Water, including emotions and issues of the heart.  This card represents " + attribute
    elif self.suit == "Wands":
      attribute = wands_attributes[self.number]
      return "The suit of Wands reflects elemental Fire, including passion, drive and career.  This card represents " + attribute
    elif self.suit == "Swords":
      attribute = swords_attributes[self.number]
      return "The suit of Swords reflects elemental Air, including thoughts, ideas and the stories we tell.  The card represents " + attribute
    elif self.suit == "Pentacles":
        attribute = pentacles_attributes[self.number]
        return "The suit of Pentacles reflects elemental Earth, including health, money and all things tangible.  The card represents " + attribute 

# Create class for 'spread': 
# Uses input to generate card representing past, present and future 
# Uses random to decided between Major and Minor when numbers overlap (0-13)
# If Minor, uses random to generate suit
class Spread:
    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third

    
    def generate_spread(self):
        spread = []
        if self.first > 13:
            past = Major(self.first, archetype[self.first])
        elif self.first <= 13:
            suit_gen = random.randint(0, 3)
            decider = random.randint(0,1)
            if decider <= 0.5:
                past = Minor(self.first, rank[self.first], suit[suit_gen])
            elif decider >= 0.5:
                past = Major(self.first, archetype[self.first])
          
        spread.append(past)

        if self.second > 13:
            present = Major(self.second, archetype[self.second])
        elif self.second <= 13:
            suit_gen = random.randint(1, 4)
            decider = random.randint(0,1)
            if decider <= 0.5:
                present = Minor(self.second, rank[self.second], suit[suit_gen])
            elif decider >= 0.5:
                present = Major(self.second, archetype[self.second])
         
        spread.append(present)  

        if self.third > 13:
            future = Major(self.third, archetype[self.third])
        elif self.third <= 13:
            suit_gen = random.randint(1, 4)
            decider = random.randint(0,1)
            if decider < 0.5:
                future = Minor(self.third, rank[self.third], suit[suit_gen])
            elif decider >= 0.5:
                future = Major(self.third, archetype[self.third])
         
        spread.append(future) 
        return spread
    
    
 
#Class Examples to ensure code works properly

#Empress = Major(3, "The Empress")
#World = Major(21, "The World")
#Ace_Cups = Minor(0, "Ace", "Cups")
#Queen_Cups = Minor(13, "Queen", "Cups")
#Ace_Wands = Minor(0, "Ace", "Wands")
#Ace_Swords = Minor(0, "Ace", "Swords")
#Knight_Swords = Minor(11, "Knight", "Swords")




card_1 = int(input("Please choose a number from 0 and 21 \n\n"))

card_2 = int(input("Please choose a second number from 0 to 21 \n\n"))

card_3= int(input("Please choose a third number from 0 to 21\n\n"))

spread = Spread(card_1, card_2, card_3)
fortune = spread.generate_spread()
past = fortune[0]
present = fortune[1]
future = fortune[2]

print(f"Past: \n {past} \n {past.get_attributes()}\n")

print(f"Present: \n {present} \n {present.get_attributes()}\n")

print(f"Future: \n {future} \n {future.get_attributes()}\n")
