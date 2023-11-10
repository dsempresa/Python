'''Faça um programa em python que abra e reproduza o audio de um arquivo em MP3.'''

import pygame
pygame.mixer.init()
pygame.mixer.music.load('/mp3/musica.mp3')
pygame.mixer_music.play()