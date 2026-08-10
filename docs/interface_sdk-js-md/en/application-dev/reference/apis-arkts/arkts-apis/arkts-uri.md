# @ohos.uri(URI字符串解析)

本模块提供URI字符串解析功能，支持URI各组成部分（协议、主机、端口、路径、查询参数和片段等）的提取与设置，以及URI编码/解码、比较判断、路径规范化和查询参数操作等能力。

适用于网络请求URL处理、深链接解析或数据共享URI处理等场景。

URI遵循RFC3986规范标准，不支持非标准场景解析。

> **说明：**
> 
> - 本模块同时支持ArkTS-Dyn、ArkTS-Sta。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace uri--><!--Device-unnamed-declare namespace uri-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { uri } from 'kits/@kit.ArkTS';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [URI](arkts-arkts-uri-uri-c.md) | 构造一个URI对象，并提供URI比较、路径规范化、查询参数操作、路径段追加和URI类型判断等方法。 |

