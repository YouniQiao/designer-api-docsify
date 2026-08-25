# XmlPullParser

XmlPullParser接口用于解析现有的XML文件，适用于对XML文本进行随机访问和灵活解析的场景。

**起始版本：** 8

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { xml } from 'kits/@kit.ArkTS';
```

## constructor

```TypeScript
constructor(buffer: ArrayBuffer | DataView, encoding?: string)
```

构造并返回一个XmlPullParser对象。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer \| DataView | 是 |
| encoding | string | 否 |

## parse

```TypeScript
parse(option: ParseOptions): void
```

该接口用于根据指定的解析选项解析XML文本。

**起始版本：** 8

**废弃版本：** 14

**替代接口：** [parseXml](#parsexml)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| option | [ParseOptions](arkts-arkts-json-parseoptions-i.md) | 是 |

## parseXml

```TypeScript
parseXml(option: ParseOptions): void
```

解析XML，调用后将根据ParseOptions中配置的回调函数触发相应的解析事件，通过回调函数传递标签、属性、文本等解析信息。

**起始版本：** 14

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| option | [ParseOptions](arkts-arkts-json-parseoptions-i.md) | 是 |
