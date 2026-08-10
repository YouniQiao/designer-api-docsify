# PiPConfiguration

创建画中画控制器时的参数。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 26.0.0.

<!--Device-PiPWindow-interface PiPConfiguration--><!--Device-PiPWindow-interface PiPConfiguration-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { PiPWindow } from 'kits/@kit.ArkUI';
```

## componentController

```TypeScript
componentController: XComponentController
```

表示原始[XComponent](../../apis-arkui/arkts-components/arkts-arkui-xcomponent-i)控制器。

**Type:** [XComponentController](../arkts-components/arkts-arkui-xcomponentcontroller-c.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PiPConfiguration-componentController: XComponentController--><!--Device-PiPConfiguration-componentController: XComponentController-End-->

**System capability:** SystemCapability.Window.SessionManager

## contentHeight

```TypeScript
contentHeight?: int
```

原始内容高度，单位为px。用于确定画中画窗口比例。当  
[使用typeNode的方式](arkts-arkui-pipwindow-create-f.md#create)创建PiPController时，不传值则默认为1080。当[不使用typeNode的方式](arkts-arkui-pipwindow-create-f.md#create)创建PiPController时，不传值则默认为[XComponent](arkts-arkui-xcomponent-xcomponent-f.md#xcomponent)组件的高度。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PiPConfiguration-contentHeight?: int--><!--Device-PiPConfiguration-contentHeight?: int-End-->

**System capability:** SystemCapability.Window.SessionManager

## contentWidth

```TypeScript
contentWidth?: int
```

原始内容宽度，单位为px。用于确定画中画窗口比例。当  
[使用typeNode的方式](arkts-arkui-pipwindow-create-f.md#create)创建PiPController时，不传值则默认为1920。当[不使用typeNode的方式](arkts-arkui-pipwindow-create-f.md#create)创建PiPController时，不传值则默认为[XComponent](arkts-arkui-xcomponent-xcomponent-f.md#xcomponent)组件的宽度。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PiPConfiguration-contentWidth?: int--><!--Device-PiPConfiguration-contentWidth?: int-End-->

**System capability:** SystemCapability.Window.SessionManager

## context

```TypeScript
context: BaseContext
```

表示上下文环境。

**Type:** [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PiPConfiguration-context: BaseContext--><!--Device-PiPConfiguration-context: BaseContext-End-->

**System capability:** SystemCapability.Window.SessionManager

## controlGroups

```TypeScript
controlGroups?: Array<PiPControlGroup>
```

画中画控制面板的可选控件组列表，应用可以对此进行配置以决定是否显示。应用未配置时，面板显示基础控件（如视频播放控件组的播放/暂停控件）；应用选择配置时，则最多可以选择三个控件，超出三个create接口抛出401错误码。

**Type:** Array&lt;PiPControlGroup&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PiPConfiguration-controlGroups?: Array<PiPControlGroup>--><!--Device-PiPConfiguration-controlGroups?: Array<PiPControlGroup>-End-->

**System capability:** SystemCapability.Window.SessionManager

## cornerAdsorptionEnabled

```TypeScript
cornerAdsorptionEnabled?: boolean
```

是否开启画中画四角吸附功能。当开启画中画四角吸附功能后，屏幕将被划分为四个热区：以屏幕的上下中线和左右中线为界，形成左上、右上、左下、右下四个区域。画中画拉起时会根据上次画中画消失的位置出现在屏幕对应的角落，用户拖动窗口时可自由移动，松手后则会自动吸附在屏幕边缘。

true：表示开启画中画四角吸附功能。

false：表示关闭画中画四角吸附功能。

不传值则为默认值true。

该接口在Phone、Tablet设备上可正常调用，在其他设备上不生效。

**Type:** boolean

**Default:** true

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-PiPConfiguration-cornerAdsorptionEnabled?: boolean--><!--Device-PiPConfiguration-cornerAdsorptionEnabled?: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

## customUIController

```TypeScript
customUIController?: NodeController
```

自定义UI控制器，用于实现在画中画界面的自定义UI功能。此参数不填时，默认不使用自定义UI功能

**Type:** [NodeController](arkts-arkui-nodecontroller-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PiPConfiguration-customUIController?: NodeController--><!--Device-PiPConfiguration-customUIController?: NodeController-End-->

**System capability:** SystemCapability.Window.SessionManager

## defaultWindowSizeType

```TypeScript
defaultWindowSizeType?: int
```

当前应用第一次拉起画中画的窗口大小。

0：代表不设置大小。按照上个应用的画中画关闭前的大小启动；

1：代表小窗；

2：代表大窗；

不传值则为默认值0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PiPConfiguration-defaultWindowSizeType?: int--><!--Device-PiPConfiguration-defaultWindowSizeType?: int-End-->

**System capability:** SystemCapability.Window.SessionManager

## handleId

```TypeScript
handleId?: int
```

navigation控件下的子页面ID，点击"恢复全屏窗口"按钮后，恢复到指定的页面。只适用于UIAbility使用[Navigation](arkts-arkui-navigation-navigation-f.md#navigation)管理页面的场景，可以设置为Navigation下的子页面ID。默认为-1，恢复Navigation栈顶页面。推荐使用方法[getUniqueId()](../arkts-components/arkts-arkui-basecustomcomponent-c.md/arkts-arkui-basecustomcomponent-c.md#getuniqueid)获取页面ID。使用[Navigation](arkts-arkui-navigation-navigation-f.md#navigation)模块内页面路由时，推荐使用[系统路由表](../../../ui/arkts-navigation-cross-package.md#系统路由表)，否则可能会出现[getUniqueId()](../arkts-components/arkts-arkui-basecustomcomponent-c.md/arkts-arkui-basecustomcomponent-c.md#getuniqueid)获取页面ID不准确的情况。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Default:** -1

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-PiPConfiguration-handleId?: int--><!--Device-PiPConfiguration-handleId?: int-End-->

**System capability:** SystemCapability.Window.SessionManager

## localStorage

```TypeScript
localStorage?: LocalStorage
```

页面级别的UI状态存储单元。多实例下可用来跟踪主窗实例的UI状态存储对象，不传值则无法通过画中画窗口获取主窗的UI状态存储对象。

**Type:** [LocalStorage](arkts-arkui-localstorage-c.md)

**Since:** 17

**ArkTS mode:** ArkTS-Dyn since version 17; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 17.

<!--Device-PiPConfiguration-localStorage?: LocalStorage--><!--Device-PiPConfiguration-localStorage?: LocalStorage-End-->

**System capability:** SystemCapability.Window.SessionManager

## navigationId

```TypeScript
navigationId?: string
```

navigation控件ID，不传值则默认不需要缓存页面。

1、UIAbility使用[Navigation](arkts-arkui-navigation-navigation-f.md#navigation)管理页面时，需要设置Navigation控件的id属性，并将该id设置给画中画控制器，确保还原场景下能够从画中画窗口恢复到原页面。

2、UIAbility使用[Router](arkts-router.md)管理页面时，无需设置navigationId。

3、UIAbility只有单页面时，无需设置navigationId，还原场景下也能够从画中画窗口恢复到原页面。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PiPConfiguration-navigationId?: string--><!--Device-PiPConfiguration-navigationId?: string-End-->

**System capability:** SystemCapability.Window.SessionManager

## templateType

```TypeScript
templateType?: PiPTemplateType
```

模板类型，用以区分视频播放、视频通话、视频会议或视频直播，不传值则默认为视频播放模板。

**Type:** [PiPTemplateType](arkts-arkui-pipwindow-piptemplatetype-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PiPConfiguration-templateType?: PiPTemplateType--><!--Device-PiPConfiguration-templateType?: PiPTemplateType-End-->

**System capability:** SystemCapability.Window.SessionManager

