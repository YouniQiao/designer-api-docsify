# SuppressWarnings

系统提供的API告警屏蔽功能，允许开发者通过注解的方式抑制API调用时产生的告警。该功能可应用于类、函数、变量、类型、接口等API元素上。在源码中添加相应标注后，编译器会根据预设规则自动屏蔽对应的告警信息。预设规则包括：当API调用版本高于兼容版本时产生的兼容性告警、当设备不支持某系统能力时产生的多设备告警、当缺少权限配置时产生的权限告警等。适用于需要在特定场景下暂时忽略某些告警、避免编译器产生干扰性警告的情况，帮助开发者专注于关键问题，提高开发效率。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为23。

<!--Device-unnamed-export @interface SuppressWarnings--><!--Device-unnamed-export @interface SuppressWarnings-End-->

**系统能力：** SystemCapability.Base

## rules

```TypeScript
rules: Array<SuppressWarningsType>
```

支持告警消除的规则集合，用于指定需要抑制的告警类型。可通过数组传入多个规则同时抑制多种告警，数组至少包含一个元素。可选取值参见[SuppressWarningsType](arkts-basicservices-annotation-suppresswarningstype-e.md#SuppressWarningsType)。建议仅在明确告警不影响应用功能或已做兼容性处理时使用，避免掩盖潜在问题。

**类型：** Array&lt;[SuppressWarningsType](arkts-basicservices-annotation-suppresswarningstype-e.md)&gt;

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本23开始，该接口支持在ArkTS卡片中使用。

<!--Device-SuppressWarnings-rules: Array<SuppressWarningsType>--><!--Device-SuppressWarnings-rules: Array<SuppressWarningsType>-End-->

**系统能力：** SystemCapability.Base

