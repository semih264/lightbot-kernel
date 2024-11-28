{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "70e6ce34-78f6-4d44-a85b-76d7f9973812",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Position: [0, 1], Direction: up, Light Status: off\n",
      "Position: [0, 1], Direction: right, Light Status: off\n",
      "Position: [1, 1], Direction: right, Light Status: off\n",
      "Position: [1, 1], Direction: right, Light Status: off\n",
      "Position: [1, 1], Direction: right, Light Status: on\n",
      "Position: [1, 1], Direction: up, Light Status: on\n",
      "Position: [1, 1], Direction: up, Light Status: on\n",
      "Position: [1, 2], Direction: up, Light Status: off\n"
     ]
    }
   ],
   "source": [
    "# 10x10 rastgele yükseklik ve ışık durumu içeren arazi\n",
    "import random\n",
    "\n",
    "terrain = [[[random.randint(0, 2), 'off'] for _ in range(10)] for _ in range(10)]\n",
    "\n",
    "# Botun başlangıç durumunu belirleyin\n",
    "bot_position = [0, 0]  # x, y koordinatları\n",
    "bot_direction = 'up'   # 'up', 'down', 'left', 'right'\n",
    "\n",
    "# Komutları işleyecek bir fonksiyon yazın\n",
    "def move_bot(command):\n",
    "    global bot_position, bot_direction\n",
    "    x, y = bot_position\n",
    "    current_height = terrain[y][x][0]\n",
    "    \n",
    "    if command == '^':\n",
    "        # Bot ileri hareket edecek\n",
    "        if bot_direction == 'up' and y < 9:\n",
    "            bot_position[1] += 1\n",
    "        elif bot_direction == 'down' and y > 0:\n",
    "            bot_position[1] -= 1\n",
    "        elif bot_direction == 'left' and x > 0:\n",
    "            bot_position[0] -= 1\n",
    "        elif bot_direction == 'right' and x < 9:\n",
    "            bot_position[0] += 1\n",
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
    "        terrain[y][x][1] = 'on' if terrain[y][x][1] == 'off' else 'off'\n",
    "    elif command == '*':\n",
    "        # Zıplama işlemi (fark yalnızca 1 ise zıpla)\n",
    "        if bot_direction == 'up' and y < 9:\n",
    "            next_height = terrain[y + 1][x][0]\n",
    "            if abs(next_height - current_height) == 1:\n",
    "                bot_position[1] += 1\n",
    "        elif bot_direction == 'down' and y > 0:\n",
    "            next_height = terrain[y - 1][x][0]\n",
    "            if abs(next_height - current_height) == 1:\n",
    "                bot_position[1] -= 1\n",
    "        elif bot_direction == 'left' and x > 0:\n",
    "            next_height = terrain[y][x - 1][0]\n",
    "            if abs(next_height - current_height) == 1:\n",
    "                bot_position[0] -= 1\n",
    "        elif bot_direction == 'right' and x < 9:\n",
    "            next_height = terrain[y][x + 1][0]\n",
    "            if abs(next_height - current_height) == 1:\n",
    "                bot_position[0] += 1\n",
    "    print(f\"Position: {bot_position}, Direction: {bot_direction}, Light Status: {terrain[bot_position[1]][bot_position[0]][1]}\")\n",
    "\n",
    "# Komut dizisi çalıştırma\n",
    "commands = ['^', '>', '^', '*', '@', '<', '*', '^']\n",
    "for cmd in commands:\n",
    "    move_bot(cmd)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7c032dab-0d7b-4033-95e8-51072e32475b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4a4e3eb8-9b39-46db-b647-cc6ff252f53c",
   "metadata": {},
   "outputs": [],
   "source": []
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
