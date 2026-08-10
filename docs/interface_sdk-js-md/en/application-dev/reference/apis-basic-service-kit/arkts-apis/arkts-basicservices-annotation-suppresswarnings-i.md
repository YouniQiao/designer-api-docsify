# SuppressWarnings

系统提供的API告警屏蔽功能，允许开发者通过注解的方式抑制API调用时产生的告警。该功能可应用于类、函数、变量、类型、接口等API元素上。在源码中添加相应标注后，编译器会根据预设规则自动屏蔽对应的告警信息。预设规则包括：当API调用版本高于兼容版本时产生的兼容性告警、当设备不支持某系统能力时产生的多设备告警、当缺少权限配置时产生的权限告警等。适用于需要在特定场景下暂时忽略某些告警、避免编译器产生干扰性警告的情况，帮助开发者专注于关键问题，提高开发效率。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-unnamed-export @interface SuppressWarnings--><!--Device-unnamed-export @interface SuppressWarnings-End-->

**System capability:** SystemCapability.Base

## Modules to Import

```TypeScript
import { SuppressWarnings, Available, SuppressWarningsType } from 'kits/@kit.BasicServicesKit';
```

## rules

```TypeScript
rules: Array<SuppressWarningsType>
```

支持告警消除的规则集合，用于指定需要抑制的告警类型。可通过数组传入多个规则同时抑制多种告警，数组至少包含一个元素。可选取值参见[SuppressWarningsType](arkts-basicservices-annotation-suppresswarningstype-e.md)。建议仅在明确告警不影响应用功能或已做兼容性处理时使用，避免掩盖潜在问题。

**Type:** Array&lt;SuppressWarningsType&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-SuppressWarnings-rules: Array<SuppressWarningsType>--><!--Device-SuppressWarnings-rules: Array<SuppressWarningsType>-End-->

**System capability:** SystemCapability.Base

