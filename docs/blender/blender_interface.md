# Interface do Blender

[Documentação](https://docs.blender.org/manual/en/2.90/interface/index.html#user-interface)

![interface](../figs/imgBlender/blenderInterface.jpg)

1. Menu do programa (application menu)
2. Workspaces (interface com formato de abas)
3. Controles de cena e camadas de visibilidade (Scene and View Layer selection)
4. Áreas / Editores

Os Workspaces servem para trocar entre diferentes configurações de Áreas e Editores.

_______________
# Áreas

Redimensionando Áreas:

![img](../figs/imgBlender/interface/areas_redim.gif)


![img](../figs/imgBlender/interface/areas.png)

________________
## Editores

[Documentação](https://docs.blender.org/manual/en/2.90/editors/index.html#editors)

Toda Áreas é ocupada por um editor, que pode ser trocado na caixa de seleção na posição superior esquerda (por padrão) da respectiva área. 

![Editores](../figs/imgBlender/blendeditors.jpg)

  1. 3D Viewport
   
  2. Outliner
   
     a. View Layer

  3. Properties

  4. Timeline


O atalho ``ctrl`` + ``space`` maximiza o editor atual ou retorna para a vista padrão da aba.

________________
## Navegação

### Atalhos

Zoom: `MMB` (Rolar)
PAN : `SHIFT` + `MMB` (Arrastar)
ORBIT: `MMB` (Arrastar)

### Navigation Gizmo

![img](../figs/imgBlender/interface/NAVIG_GIZMO.jpg)


### Configuração modo de Zoom


Abra a janela de preferências (Edit -> Preferences ou `F4` seguido da tecla `P`)

Para o Zoom centralizar na posição do mouse
![img](../figs/imgBlender/CONFIG_NAV.jpg)


________________
## Temas e presets

![img](../figs/imgBlender/interface/themes_presets.gif)



________________

## Painéis T e N

Alguns editores possuem pequenas setas nos lados de duas áreas. Menus podem ser abertos clicando e arrastando nas setas, ou pelos atalhos ``T`` e ``N``.

Abaixo Vemos a indicação das setas no editor 3d Viewport.

![menus T e N](../figs/imgBlender/menusTeN.jpg)

No Lado esquerdo, temos o painel de ferramentas (tools panel) que pode ser visto ou escondido teclando ``T``.

![Menu T](../figs/imgBlender/menuT.jpg)

No lado direito temos o painel lateral (Sidebar panel), que pode ser mostrado ou recolhido também pela tecla ``N``(como muitos dos ajustes são numéricos, a equipe do Blender escolheu a tecla ``N`` como atalho para este painel)

![Menu N](../figs/imgBlender/menuN.jpg)

É comum encontrar estes paineis referidos como ``T`` e ``N`` nos materiais de informação sobre o blender.

Uma outra versão do painel T pode ser vista pressionando as teclas ``shift + space``. 

![shift+space](../figs/imgBlender/shifht_space.jpg)

Uma tabela com botões aparece na posição do ponteiro do mouse, apresentando os mesmos botões do painel de ferramentas. 

________________

## Modos de Trabalho do Editor 3D Viewport

Os modos de trabalho ([object modes](https://docs.blender.org/manual/en/2.90/editors/3dview/modes.html#object-modes) podem ser selecionados pela barra superior esquerda do editor 3d viewport.

![modos](../figs/imgBlender/modosobj.jpg)

Selecione um dos objetos da cena e clique na seta do seletor de modos como na figura acima.

Apenas dois modos de objeto serão apresentados neste momento, **Object Mode** e o **Edit Mode**. A tecla ``Tab`` alterna automaticamente entre estes dois modos.

**Observação:** note que, quando mudamos de modo os painéis mostram algumas opções diferentes.

_______________

## Precisão (snaps & pivots)

![snaps](../figs/imgBlender/snaps.png)

Comandos de precisão do Blender.

![pivots](../figs/imgBlender/pivot.png)

Pontos pivots de transformação do Blender.

_______________

## Sistemas de coordenadas

![Coordenadas_Blender](../figs/imgBlender/coordenadas_blender.jpg)

1. Global
2. Local
3. Normal
4. Gimbal
5. View
6. Cursor
7. A partir de um objeto (+)

________________

