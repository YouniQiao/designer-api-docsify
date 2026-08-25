# @ohos.xml(XML解析与生成)

本模块提供XML生成和解析的接口，支持多种方式的XML文本生成与解析，可帮助开发者高效处理结构化XML数据。本模块提供了两种生成XML文件的方式:  
* [XmlSerializer](arkts-arkts-xml-xmlserializer-c.md)：适用于已知XML文本大小的情况。需要开发者自行创建ArrayBuffer作为缓存区域，需确保缓存区域足以容纳生成的文本内容。  
* [XmlDynamicSerializer&lt;sup&gt;20+&lt;/sup&gt;](arkts-arkts-xml-xmldynamicserializer-c.md)：适用于未知XML文本大小的情况。无需自行创建ArrayBuffer，程序动态扩容，但序列化结果字符串长度上限为100000。本模块提供了两种解析XML文件的方式:  
* [XmlPullParser](arkts-arkts-xml-xmlpullparser-c.md)：适用于对XML文本进行随机访问和灵活解析的场景。  
* [XmlSAXParser&lt;sup&gt;24+&lt;/sup&gt;](arkts-arkts-xml-xmlsaxparser-c.md)：适用于流式解析XML文本的场景，当XML文本较大，其他解析方式会消耗较多内存，建议采用流式解析。

> **说明：**&gt;
> - 本模块同时支持ArkTS-Dyn、ArkTS-Sta。

**起始版本：** 8

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { xml } from 'kits/@kit.ArkTS';
```

## 汇总

### 类

| 名称 |
| --- |
| [XmlDynamicSerializer(XML解析与生成)](arkts-arkts-xml-xmldynamicserializer-c.md) |
| [XmlPullParser(XML解析与生成)](arkts-arkts-xml-xmlpullparser-c.md) |
| [XmlSAXParser(XML解析与生成)](arkts-arkts-xml-xmlsaxparser-c.md) |
| [XmlSerializer(XML解析与生成)](arkts-arkts-xml-xmlserializer-c.md) |

### 接口

| 名称 |
| --- |
| [ParseInfo(XML解析与生成)](arkts-arkts-xml-parseinfo-i.md) |
| [ParseOptions(XML解析与生成)](arkts-arkts-xml-parseoptions-i.md) |
| [XmlSAXHandler(XML解析与生成)](arkts-arkts-xml-xmlsaxhandler-i.md) |

### 枚举

| 名称 |
| --- |
| [EventType(XML解析与生成)](arkts-arkts-xml-eventtype-e.md) |

### 类型

| 名称 |
| --- |
| [AttributeWithTagCb(XML解析与生成)](arkts-arkts-xml-attributewithtagcb-t.md) |
