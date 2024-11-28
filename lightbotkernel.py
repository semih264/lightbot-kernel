{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "805b015e-4afd-478a-828e-baa47e8b86b3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 10x10 düz arazi (her hücrede [yükseklik, ışık_durumu])\n",
    "terrain = [[[0, 'off'] for _ in range(10)] for _ in range(10)]\n",
    "\n",
    "# Botun başlangıç durumunu belirleyin\n",
    "bot_position = [0, 0]  # x, y koordinatları\n",
    "bot_direction = 'up'   # 'up', 'down', 'left', 'right'\n",
    "\n",
    "# Komutları işleyecek bir fonksiyon yazın\n",
    "def move_bot(command):\n",
    "    global bot_position, bot_direction\n",
    "    if command == '^':\n",
    "        # Bot ileri hareket edecek\n",
    "        if bot_direction == 'up':\n",
    "            bot_position[1] = min(bot_position[1] + 1, 9)  # Y sınırını kontrol et\n",
    "        elif bot_direction == 'down':\n",
    "            bot_position[1] = max(bot_position[1] - 1, 0)\n",
    "        elif bot_direction == 'left':\n",
    "            bot_position[0] = max(bot_position[0] - 1, 0)\n",
    "        elif bot_direction == 'right':\n",
    "            bot_position[0] = min(bot_position[0] + 1, 9)\n",
    "    elif command == '>':\n",
    "        # Bot sağa dönecek\n",
    "        if bot_direction == 'up':\n",
    "            bot_direction = 'right'\n",
    "        elif bot_direction == 'right':\n",
    "            bot_direction = 'down'\n",
    "        elif bot_direction == 'down':\n",
    "            bot_direction = 'left'\n",
    "        elif bot_direction == 'left':\n",
    "            bot_direction = 'up'\n",
    "    elif command == '<':\n",
    "        # Bot sola dönecek\n",
    "        if bot_direction == 'up':\n",
    "            bot_direction = 'left'\n",
    "        elif bot_direction == 'left':\n",
    "            bot_direction = 'down'\n",
    "        elif bot_direction == 'down':\n",
    "            bot_direction = 'right'\n",
    "        elif bot_direction == 'right':\n",
    "            bot_direction = 'up'\n",
    "    elif command == '@':\n",
    "        # Işığı açıp kapama\n",
    "        x, y = bot_position\n",
    "        terrain[y][x][1] = 'on' if terrain[y][x][1] == 'off' else 'off'\n",
    "    print(f\"Position: {bot_position}, Direction: {bot_direction}, Light Status: {terrain[bot_position[1]][bot_position[0]][1]}\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
