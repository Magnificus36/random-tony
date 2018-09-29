#!/usr/bin/env python3

import cfg_generator
import logging
from tony_cfg import tony_en
from tony_cfg import tony_nl

def format_output(generatedoutput):
    ingredients = list(cfg_generator.flatten(generatedoutput))
    logging.info("joining everything with spaces")
    smaak = ' '.join(ingredients)
    logging.info("removing space before comma")
    return smaak.replace(" ,", ",")

def generate_tony_flavours_en(cnt):
    ldg = cfg_generator.Grammar() # limited_edition_grammar
    ldg.parse_grammar(tony_en)
    for i in range(0,cnt):
        generatedoutput = ldg.generate('S')
        #print('-'.join(flatten(ldg.generate('S'))))
        print(format_output(generatedoutput))

def generate_tony_flavours_nl(cnt):
    ldg = cfg_generator.Grammar() # limited_edition_grammar
    ldg.parse_grammar(tony_nl)
    for i in range(0,cnt):
        generatedoutput = ldg.generate('S')
        #print('-'.join(flatten(ldg.generate('S'))))
        print(format_output(generatedoutput))

if __name__ == "__main__":
     generate_tony_flavours_en(10)
