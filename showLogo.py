#!/usr/bin/python

import os
import time
import random

"""
TODO: Hacer que cada vez que se abra el programa salga de un color diferente.
"""

colors = ['\x1b[0;30m', '\x1b[0;31m', '\x1b[0;32m', '\x1b[0;33m', '\x1b[0;34m', '\x1b[0;35m', '\x1b[0;36m', '\x1b[0;37m', ]

thinkpadDict = {'first' : '''
{color[0]}                        {color[1]}___        {color[2]}               {color[3]}___           {color[4]}___
{color[0]}                       {color[1]}/\  \       {color[2]}              {color[3]}/\  \         {color[4]}/|  |
{color[0]}            ___        {color[1]}\:\  \       {color[2]}___          {color[3]}\:\  \       {color[4]}|:|  |
{color[0]}           /\__\        {color[1]}\:\  \     {color[2]}/\__\          {color[3]}\:\  \      {color[4]}|:|  |
{color[0]}          /:/  /    {color[1]}___ /::\  \   {color[2]}/:/__/      {color[3]}_____\:\  \   {color[4]}__|:|  |
{color[0]}         /:/__/    {color[1]}/\  /:/\:\__\ {color[2]}/::\  \     {color[3]}/::::::::\__\ {color[4]}/\ |:|__|____
{color[0]}        /::\  \    {color[1]}\:\/:/  \/__/ {color[2]}\/\:\  \__  {color[3]}\:\~~\~~\/__/ {color[4]}\:\/:::::/__/
{color[0]}       /:/\:\  \    {color[1]}\::/__/       {color[2]}~~\:\/\__\  {color[3]}\:\  \        {color[4]}\::/~~/~
{color[0]}       \/__\:\  \    {color[1]}\:\  \          {color[2]}\::/  /   {color[3]}\:\  \        {color[4]}\:\~~\\
{color[0]}            \:\__\    {color[1]}\:\__\         {color[2]}/:/  /     {color[3]}\:\__\        {color[4]}\:\__\\
{color[0]}             \/__/     {color[1]}\/__/         {color[2]}\/__/       {color[3]}\/__/         {color[4]}\/__/
''',

'second' : '''
{color[0]}                        {color[1]}___        {color[2]}               {color[3]}___           {color[4]}___
{color[0]}                       {color[1]}/\  \       {color[2]}              {color[3]}/\  \         {color[4]}/|  |
{color[0]}            ___        {color[1]}\:\  \       {color[2]}___          {color[3]}\:\  \       {color[4]}|:|  |
{color[0]}           /\__\        {color[1]}\:\  \     {color[2]}/\__\          {color[3]}\:\  \      {color[4]}|:|  |
{color[0]}          /:/  /    {color[1]}___ /::\  \   {color[2]}/:/__/      {color[3]}_____\:\  \   {color[4]}__|:|  |
{color[0]}         /:/__/    {color[1]}/\  /:/\:\__\ {color[2]}/::\  \     {color[3]}/::::::::\__\ {color[4]}/\ |:|__|____
{color[0]}        /::\  \    {color[1]}\:\/:/  \/__/ {color[2]}\/\:\  \__  {color[3]}\:\~~\~~\/__/ {color[4]}\:\/:::::/__/
{color[0]}       /:/\:\  \    {color[1]}\::/__/       {color[2]}~~\:\/\__\  {color[3]}\:\  \        {color[4]}\::/~~/~
{color[0]}       \/__\:\  \    {color[1]}\:\  \          {color[2]}\::/  /   {color[3]}\:\  \        {color[4]}\:\~~\\
{color[0]}            \:\__\    {color[1]}\:\__\         {color[2]}/:/  /     {color[3]}\:\__\        {color[4]}\:\__\\
{color[0]}             \/__/     {color[1]}\/__/         {color[2]}\/__/       {color[3]}\/__/         {color[4]}\/__/
{color[2]}                          ___         {color[5]}___
{color[2]}                         /\  \       {color[5]}/\  \         {color[6]}_____
{color[2]}                        /::\  \     {color[5]}/::\  \       {color[6]}/::\  \\
{color[2]}                       /:/\:\__\   {color[5]}/:/\:\  \     {color[6]}/:/\:\  \\
{color[2]}                      /:/ /:/  /  {color[5]}/:/ /::\  \   {color[6]}/:/  \:\__\\
{color[2]}                     /:/_/:/  /  {color[5]}/:/_/:/\:\__\ {color[6]}/:/__/ \:|__|
{color[2]}                     \:\/:/  /   {color[5]}\:\/:/  \/__/ {color[6]}\:\  \ /:/  /
{color[2]}                      \::/__/     {color[5]}\::/__/       {color[6]}\:\  /:/  /
{color[2]}                       \:\  \      {color[5]}\:\  \        {color[6]}\:\/:/  /
{color[2]}                        \:\__\      {color[5]}\:\__\        {color[6]}\::/  /
{color[2]}		         \/__/       {color[5]}\/__/         {color[6]}\/__/
'''}

print(thinkpadDict['first'].format(color=colors[:5]))
time.sleep(0.5)
os.system('clear')
print(thinkpadDict['second'].format(color=colors))
time.sleep(0.5)
os.system('clear')
