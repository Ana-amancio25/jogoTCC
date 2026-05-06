
define aria = Character("Aria")
define nathaniel = Character("Nathaniel")
define alan = Character("Alan")
define monica = Character("Mônica")
define penelope = Character("Penélope")

image sala = "sala.jpeg"
image corredor = "corredor3.jpg"
image secretaria = "secretaria.jpg"
image ar = "ar.png"
image na = "na.png"
image al = "al.png"
image mo = "mo.png"
image pe = "pe.png"

default rel_nathaniel = 0
default rel_penelope = 0
default rel_alan = 0


default saude = 5

default pa = 10

screen objetivo:

    frame:
        xalign 0.5
        yalign 0.5
        background "#0008"
        padding (15, 10)

        text "OBJETIVO: [objetivo_atual]" size 40 color "#ffd503" 

label tomar_dano(valor):

    $ saude -= valor

    show screen status_saude

    "Você perdeu -[valor] de saúde."

    hide screen status_saude

    if saude <= 0:
        jump game_over

    return

label game_over:

    scene black
    "Seus ferimentos foram graves demais..."
    "Você não sobreviveu."

    return

screen resumo_dia:

    frame:
        xalign 0.5
        yalign 0.5
        padding (30, 30)

        vbox:
            spacing 10

            text "Resumo do Dia" size 40

            text "Saúde: [saude]"

            text "Relacionamentos:"

            text "Nathaniel: [rel_nathaniel]%"
            text "Penélope: [rel_penelope]%"
            text "Alan: [rel_alan]%"


            textbutton "Continuar" action Return()


screen status_saude:

    hbox:
        xalign 0.02
        yalign 0.02
        spacing 5

        text "❤️" size 35

        if saude <= 2:
            text "[saude]" color "#f87000" size 30
        else:
            text "[saude]" color "#ffffff" size 30


screen status_pa:

    hbox:
        xalign 0.02
        yalign 0.08
        spacing 5

        text "⚡" size 35

        if pa <= 1:
            text "[pa]" color "#ff0" size 30
        else:
            text "[pa]" color "#ffffff" size 30

screen status_rel:

    frame:
        xalign 0.98
        yalign 0.02
        padding (15, 15)
        background "#0008"

        vbox:
            spacing 5

            text "Relações" color "#fff"

            text "Nathaniel: [rel_nathaniel]%" color "#fff"
            text "Penélope: [rel_penelope]%" color "#fff"
            text "Alan: [rel_alan]%" color "#fff"
 
    

label start:

    play music "tema.mp3"
  
    scene sala
    

    $ objetivo_atual = "Descobrir o que está acontecendo e sobreviver"

    "Enquanto todos fugiam, ao ver pessoas gritando e correndo para fora de um dos campus, você, Aria procura onde se esconder dentro do campus de jornalismo e acaba entrando em uma sala"
    "Mas assim que entra percebe que lá já haviam mais 3 pessoas."

    show screen objetivo

    "Uma discussão estava acontecendo e quando a porta é aberta ela se cessa."

    hide screen objetivo

    hide ar

    show na
    nathaniel "MAIS UM?!"
    hide na

    show al
    alan "Ela parece estar normal para você?"
    hide al


    show ar
menu:

    "Aria: Eu pareço esquisita?":
        hide ar
        show pe 

        penelope "Todos parecem, mas parece que ela está limpa."
        hide pe
        


    "Aria: Eu estou normal":
        hide ar
        
show ar

menu:

    "Aria: Me deixem ficar, por favor":
        hide ar
        


    "Aria: Claro que estou":
        hide ar
        

show al
alan "Você fica então."
hide al

show na
nathaniel "É sério isso?"
hide na


"Os outros voltam a discutir, mas você, que é a mais próxima da porta escuta um barulho do outro lado. Você espera ou reage?"

show ar

menu:

    "Esperar a discussão terminar para ver o que fazer.":
        jump cena1
    
    "Reagir e avisar o grupo agora.":
        jump cena2


label cena1:

    scene sala
    "Uma criatura invade a sala quebrando tudo."
    show na
    nathaniel "Resolve essa agora!"
    hide na

    show pe
    penelope "Vamos sair daqui!"
    hide pe

    "Antes mesmo de poder reagir a criatura corre pra cima de você."

show ar
menu:
    "Tentar dar um soco":
        show screen status_pa

        if pa >= 3:
            $ pa -= 3
            "Você mira na cara dele e dá um soco com toda sua força gantando 3PA."
            "Ele fica atordoado por alguns segundos, tempo suficiente para você fugir."
        else:
            "Você não tem energia suficiente para atacar."

        hide screen status_pa

    "Tentar fugir":     
        "Você tenta correr para longe da porta mas a criatura te empurra fazendo você cair em cima de uma das carteiras" 
        call tomar_dano(0.5)
        
        
        show na
        "Nathaniel pega uma das cadeiras a sua volta e  joga no zumbi"
        hide na

hide ar

show al
alan "Vamos sair daqui e encontrar um outro lugar!"
hide al

show pe
penelope "Parabéns por pensar o óbvio gênio."
hide pe

show ar
aria "Aria: Vamos logo!"
hide ar

scene corredor
"Vocês correm para longe da sala e veem o corredor deserto sem nenhuma alma viva, mas vocês continuam a fuga."

show al
alan "Vamos procurar um outro lugar."
hide al

show na
nathaniel "E você pretende ir para onde?"
hide na

show pe
penelope "Ficar aqui com certeza não é uma opção."
hide pe

show ar
aria "Aria: Eu concordo!"
hide ar

show na
nathaniel "A gente deveria sair desse lugar o mais rápido possível."
hide na

show pe
penelope "E ir pra onde?! Não tem nada perto desse buraco de lugar a menos de 300Km!"
hide pe

show al
alan "Vamos tentar achar alguém que saiba o que esta acontecendo."
hide al


show na
nathaniel "A gente devia é achar algo pra bater nessas coisas."
hide na

show pe
penelope "Pra mim tanto faz só vamos sair daqui logo!"
hide pe

show ar
menu:
    "Aria: Concordo com o Alan, vamos tentar descobrir o que esta acontecendo primeiro antes de sair batendo em tudo.":
        $rel_alan += 5
        hide ar
        jump cena3
      
    
    "Aria: O Nathaniel tem razão, temos que nos defender.":
        $rel_nathaniel += 5
        hide ar
        jump cena4



label cena2:

scene sala

show ar

menu:
    "Aria: Escutei alguma coisa, melhor a gente sair daqui":
        hide ar

    "Aria: Fiquem quietos, tem algo vindo":
        hide ar

show pe
penelope "E pra onde a gente vai? Esse lugar não tem nada de útil."
hide pe

show al
alan "Talve-"
hide al

"Todos se calam. Sons esquisitos, quase como rosnados e é como se alguémestivesse se arrastando. Seja lá o que for,está se aproximando."
"..."
"PÁ!!!"
"A porta treme com a batida. Você sente uma dor no peito por segurar um grito. Mas, foi bem visível que todos deram um pulo junto assim como você."
"Silêncio novamente, mas a “pessoa” do lado de fora não se move mais"
"Aos poucos os sons voltam a ecoar do lado de fora da sala. O “alguém”, finalmente volta a se arrastar para outro lado"
        
show al
alan "A gente tem que sair daqui, não da pra passar o resto do dia aqui."
hide al

show pe 
penelope "Parabéns por pensar o óbvio gênio."
hide pe

show na
nathaniel "E você pretende ir para onde?"
hide na

show ar
aria "Aria: Procurar por pessoas?"
hide ar

show na
nathaniel "Se for assim, é melhor chamar o nosso amigo de volta."
hide na

"Alan abriu a porta, está na hora de sair. Vocês o seguem."

show al
alan "Vamos tentar achar alguém que saiba o que esta acontecendo."
hide al

show na
nathaniel "A gente devia é achar algo pra bater nessas coisas"
hide na

menu:
    "Aria: Concordo com o Alan, vamos tentar descobrir o que esta acontecendo primeiro antes de sair batendo em tudo.":
        $rel_alan += 5
        jump cena3
      
    
    "Aria: O Nathaniel tem razão, temos que nos defender.":
        $rel_nathaniel += 5
        jump cena4
    


label cena3:
    show screen status_rel

    show al
    alan "Vamos pra que lado então?"
    hide al

    hide screen status_rel

    show pe 
    penelope "Só me sigam."
    hide pe

    scene corredor3

    "Vocês andam rapidamente pelo corredor principal do campus de Jornalismo."

    "Chegando perto da secretaria é possível escutar vários gritos."

    scene secretaria

    "Vocês correm até porta da secretaria e veem uma mulher sentada no canto da sala com o seu braço sangrando."

    show mo
    "Ela olha para vocês com um olhar de cansaço, suas roupas estão sujas, mas ela parece assustada. "
    hide mo

show ar
menu:
    "Aria: O que aconteceu!?":
        hide ar

    "Aria: Quem é você?":
        hide ar


show pe 
penelope "Mônica?!"
hide pe

show mo 
monica "Penélope?! Estou feliz que você esteja bem!"
hide mo

"Penélope se aproxima e percebe a palidez e as manchas pretas e avermelhadas na pele da mulher."

show pe 
penelope "O que aconteceu!?"
hide pe

show mo 
monica "Eu... não sei bem."
hide mo

show na
nathaniel "Como assim você não sabe? Seu braço ta sangrando!"
hide na

show al
alan "Agora não é hora, acha alguma coisa pra gente parar o sangue!"
hide al

show mo 
monica "Eu, eu fui atacada, mas..."
hide mo

show mo 
monica "Vocês devem achar o..."
hide mo

"A mulher para um instante."

show mo 
monica "O professor de...história... o Fábio."
hide mo

"Ela tosse um pouco."

show na
nathaniel "Fábio? Onde vamos achar ele, esse lugar é enorme?!"
hide na

show mo 
monica "Acho... que ele está no campus de biologia?"
hide mo

show na
nathaniel "Acha?"
hide na

show al
alan "Agora não é hora, acha alguma coisa pra gente parar o sangue!"
hide al

show ar
aria "Aria: Calma, vamos te ajudar."
hide ar

show pe 
penelope "Onde mais você ta machucada?"
hide pe

show mo 
monica " Eu sinto um formigamento, e... muita fome."
hide mo

show ar
aria "Aria: Eu sei os primeiros socorros."
hide ar

"Você se aproxima para ver os ferimentos, mas antes que consiga chegar perto, Mônica grita e te empurra com força."
"Você cai no chão, sem entender o que acabou de acontecer."


label cena4:

      
call screen resumo_dia
return
