# CollectStrategy（系统接口）

Defines a page information collection policy.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-onScreen-export enum CollectStrategy--><!--Device-onScreen-export enum CollectStrategy-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## ALLOW

```TypeScript
ALLOW = 1 << 0
```

Collection is supported.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CollectStrategy-ALLOW = 1 << 0--><!--Device-CollectStrategy-ALLOW = 1 << 0-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## SPLIT_SCREEN

```TypeScript
SPLIT_SCREEN = 1 << 1
```

Collection policy of the split-screen window on the application.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CollectStrategy-SPLIT_SCREEN = 1 << 1--><!--Device-CollectStrategy-SPLIT_SCREEN = 1 << 1-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## UNSUPPORTED_APP

```TypeScript
UNSUPPORTED_APP = 1 << 2
```

Automatic collection is not supported.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CollectStrategy-UNSUPPORTED_APP = 1 << 2--><!--Device-CollectStrategy-UNSUPPORTED_APP = 1 << 2-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## PRIVATE_WINDOW

```TypeScript
PRIVATE_WINDOW = 1 << 3
```

Privacy window of the application.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CollectStrategy-PRIVATE_WINDOW = 1 << 3--><!--Device-CollectStrategy-PRIVATE_WINDOW = 1 << 3-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## ANCO_APP

```TypeScript
ANCO_APP = 1 << 4
```

VM application, which is a non-HarmonyOS application.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CollectStrategy-ANCO_APP = 1 << 4--><!--Device-CollectStrategy-ANCO_APP = 1 << 4-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## ALLOW_USER_CHANGE

```TypeScript
ALLOW_USER_CHANGE = 1 << 5
```

Collection policies can be configured.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CollectStrategy-ALLOW_USER_CHANGE = 1 << 5--><!--Device-CollectStrategy-ALLOW_USER_CHANGE = 1 << 5-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## BUSINESS_APP

```TypeScript
BUSINESS_APP = 1 << 6
```

Application data can be collected.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CollectStrategy-BUSINESS_APP = 1 << 6--><!--Device-CollectStrategy-BUSINESS_APP = 1 << 6-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## FLOAT_SCREEN

```TypeScript
FLOAT_SCREEN = 1 << 7
```

Floating window.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CollectStrategy-FLOAT_SCREEN = 1 << 7--><!--Device-CollectStrategy-FLOAT_SCREEN = 1 << 7-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## PIP_SCREEN

```TypeScript
PIP_SCREEN = 1 << 8
```

Picture-in-picture mode.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CollectStrategy-PIP_SCREEN = 1 << 8--><!--Device-CollectStrategy-PIP_SCREEN = 1 << 8-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## LAUNCHER

```TypeScript
LAUNCHER = 1 << 9
```

Desktop application.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CollectStrategy-LAUNCHER = 1 << 9--><!--Device-CollectStrategy-LAUNCHER = 1 << 9-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

