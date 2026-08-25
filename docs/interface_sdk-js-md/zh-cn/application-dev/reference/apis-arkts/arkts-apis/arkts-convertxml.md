# @ohos.convertxml

本模块提供将XML文本转换为JavaScript对象的解析能力，适用于XML配置文件解析、XML格式网络数据处理、数据迁移与格式转换等场景。 转换过程中，XML的各类组件（声明、指令、元素、属性、文本、CDATA、注释和Doctype等）会按照ConvertOptions中配置的键名映射为JavaScript对象的属性， 形成层级嵌套的对象结构，简化了XML数据的处理流程，支持通过ConvertOptions自定义键名映射实现灵活的输出结构。

**起始版本：** 8

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { convertxml } from 'kits/@kit.ArkTS';
```

## 汇总

### 类

| 名称 |
| --- |
| [ConvertXML](arkts-arkts-xml-convertxml-c.md) |

### 接口

| 名称 |
| --- |
| [ConvertOptions](arkts-arkts-xml-convertoptions-i.md) |
