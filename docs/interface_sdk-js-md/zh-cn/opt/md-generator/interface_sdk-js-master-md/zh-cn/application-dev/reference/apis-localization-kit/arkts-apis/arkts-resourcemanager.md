# @ohos.resourceManager

本模块提供应用资源和系统资源的访问能力，允许应用根据当前的[Configuration](arkts-localization-resourcemanager-configuration-c.md#Configuration)配置，获取最匹配的应用资源或系统资源，支持国际化资源匹配和多设备适配。具体匹配规则参考[资源匹配](../../../quick-start/resource-categories-and-access.md#资源匹配)。

Configuration配置包括语言-文字-国家地区、横竖屏、颜色模式、Mcc（移动国家码）和Mnc（移动网络码）、设备类型、屏幕密度。

**使用场景**：

- 应用国际化：根据用户语言和地区自动获取匹配的字符串资源。  
- 多设备适配：根据设备类型、屏幕密度获取合适的媒体资源。  
- 动态资源配置：根据设备状态（横竖屏、颜色模式等）获取对应配置的资源。

**使用说明**：

- FA模型需要先导入模块，再调用[getResourceManager](arkts-localization-resourcemanager-getresourcemanager-f.md#getResourceManager)接口获取资源管理对象。  
- 从API version 9开始，Stage模型无需导入模块，支持通过Context获取资源管理resourceManager对象。Context的更多介绍请参考  
[应用上下文Context](../../../application-models/application-context-stage.md)。

 ```ts  import { UIAbility } from '@kit.AbilityKit'; import { window } from '@kit.ArkUI';

 export default class EntryAbility extends UIAbility { onWindowStageCreate(windowStage: window.WindowStage) { let context = this.context; let resourceManager = context.resourceManager; } } ```

**起始版本：** 6

<!--Device-unnamed-declare namespace resourceManager--><!--Device-unnamed-declare namespace resourceManager-End-->

**系统能力：** SystemCapability.Global.ResourceManager

## 汇总

### 函数

| 名称 |
| --- |
| [getResourceManager](arkts-localization-resourcemanager-getresourcemanager-f.md#getresourcemanager) |
| [getResourceManager](arkts-localization-resourcemanager-getresourcemanager-f.md#getresourcemanager-1) |
| [getResourceManager](arkts-localization-resourcemanager-getresourcemanager-f.md#getresourcemanager-2) |
| [getResourceManager](arkts-localization-resourcemanager-getresourcemanager-f.md#getresourcemanager-3) |
| [getSysResourceManager](arkts-localization-resourcemanager-getsysresourcemanager-f.md#getsysresourcemanager) |
| [getSystemResourceManager](arkts-localization-resourcemanager-getsystemresourcemanager-f.md#getsystemresourcemanager) |

### 类

| 名称 |
| --- |
| [Configuration](arkts-localization-resourcemanager-configuration-c.md) |
| [DeviceCapability](arkts-localization-resourcemanager-devicecapability-c.md) |

### 接口

| 名称 |
| --- |
| [AsyncCallback](arkts-localization-resourcemanager-asynccallback-i.md) |
| [ResourceManager](arkts-localization-resourcemanager-resourcemanager-i.md) |

### 枚举

| 名称 |
| --- |
| [ColorMode](arkts-localization-resourcemanager-colormode-e.md) |
| [DeviceType](arkts-localization-resourcemanager-devicetype-e.md) |
| [Direction](arkts-localization-resourcemanager-direction-e.md) |
| [ScreenDensity](arkts-localization-resourcemanager-screendensity-e.md) |

### 类型

| 名称 |
| --- |
| [RawFileDescriptor](arkts-localization-resourcemanager-rawfiledescriptor-t.md) |
| [Resource](arkts-localization-resourcemanager-resource-t.md) |
