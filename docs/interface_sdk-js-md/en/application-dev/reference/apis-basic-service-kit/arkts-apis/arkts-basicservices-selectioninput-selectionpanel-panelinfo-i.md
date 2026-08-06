# PanelInfo

Defines attributes of the word selection panel, including its type, position, and size. You can specify the panel type (menu panel or main panel) using **panelType**, set the coordinates of the upper left corner of the panel using  
**x** and **y**, and set the panel size using **width** and **height**. These attributes collectively define the display form of the panel.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-unnamed-export interface PanelInfo--><!--Device-unnamed-export interface PanelInfo-End-->

**System capability:** SystemCapability.SelectionInput.Selection

## height

```TypeScript
height: int
```

Height of the word selection panel, in px. The value range is (0, +∞). If **0** or a negative value is passed, the panel cannot be created.

**Type:** int

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanelInfo-height: int--><!--Device-PanelInfo-height: int-End-->

**System capability:** SystemCapability.SelectionInput.Selection

## panelType

```TypeScript
panelType: PanelType
```

Word selection panel types, which include two options. For details, see [PanelType]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Type:** PanelType

**Default:** MENU_PANEL

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanelInfo-panelType: PanelType--><!--Device-PanelInfo-panelType: PanelType-End-->

**System capability:** SystemCapability.SelectionInput.Selection

## width

```TypeScript
width: int
```

Width of the word selection panel, in px. The value range is (0, +∞). If **0** or a negative value is passed, the panel cannot be created.

**Type:** int

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanelInfo-width: int--><!--Device-PanelInfo-width: int-End-->

**System capability:** SystemCapability.SelectionInput.Selection

## x

```TypeScript
x: int
```

X-coordinate of the upper left corner of the word selection panel, in px. The upper left corner of the main screen is the origin, and the positive direction of the X axis is rightward. The value range is  
[0, +∞). If a negative value is passed, the panel cannot be created.

**Type:** int

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanelInfo-x: int--><!--Device-PanelInfo-x: int-End-->

**System capability:** SystemCapability.SelectionInput.Selection

## y

```TypeScript
y: int
```

Y-coordinate of the upper left corner of the word selection panel, in px. The upper left corner of the main screen is the origin, and the positive direction of the Y axis is downward. The value range is  
[0, +∞). If a negative value is passed, the panel cannot be created.

**Type:** int

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanelInfo-y: int--><!--Device-PanelInfo-y: int-End-->

**System capability:** SystemCapability.SelectionInput.Selection

