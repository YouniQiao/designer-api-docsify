# console

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-unnamed-export declare class console--><!--Device-unnamed-export declare class console-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## debug

```TypeScript
static debug(message: string, ...arguments: any[]): void
```

以格式化输出方式打印调试信息。

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

**模型约束：** 此接口仅可在FA模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-console-static debug(message: string, ...arguments: any[]): void--><!--Device-console-static debug(message: string, ...arguments: any[]): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 是 | 要打印的文本信息。 |
| arguments | any[] | 是 | 其余要打印的信息或message的替换值。 |

## error

```TypeScript
static error(message: string, ...arguments: any[]): void
```

以格式化输出方式打印错误信息。

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

**模型约束：** 此接口仅可在FA模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-console-static error(message: string, ...arguments: any[]): void--><!--Device-console-static error(message: string, ...arguments: any[]): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 是 | 要打印的错误信息。 |
| arguments | any[] | 是 | 其余要打印的信息或message的替换值。 |

## info

```TypeScript
static info(message: string, ...arguments: any[]): void
```

以格式化输出方式打印日志信息（console.log()的别名）。

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

**模型约束：** 此接口仅可在FA模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-console-static info(message: string, ...arguments: any[]): void--><!--Device-console-static info(message: string, ...arguments: any[]): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 是 | 要打印的文本信息。 |
| arguments | any[] | 是 | 其余要打印的信息或message的替换值。 |

## log

```TypeScript
static log(message: string, ...arguments: any[]): void
```

以格式化输出方式打印日志信息。

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

**模型约束：** 此接口仅可在FA模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-console-static log(message: string, ...arguments: any[]): void--><!--Device-console-static log(message: string, ...arguments: any[]): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 是 | 要打印的文本信息。 |
| arguments | any[] | 是 | 其余要打印的信息或message的替换值。 |

## warn

```TypeScript
static warn(message: string, ...arguments: any[]): void
```

以格式化输出方式打印警告信息。

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

**模型约束：** 此接口仅可在FA模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-console-static warn(message: string, ...arguments: any[]): void--><!--Device-console-static warn(message: string, ...arguments: any[]): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 是 | 要打印的警告信息。 |
| arguments | any[] | 是 | 其余要打印的信息或message的替换值。 |

