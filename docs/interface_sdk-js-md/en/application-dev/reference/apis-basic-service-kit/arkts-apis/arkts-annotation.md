# @ohos.annotation(Annotation)

本模块定义了OpenHarmony ArkTS API的注解类型，如生命周期最小可用版本等。
 > **说明**
 >
 > - 本模块首批接口从 API version 22 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。


## Modules to Import

```TypeScript
import { SuppressWarnings, Available, SuppressWarningsType } from 'kits/@kit.BasicServicesKit';
```

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [Available](arkts-basicservices-annotation-available-i.md) | 系统提供的API注解能力，可用于标记API支持的最低可用版本。此注解可以标注在类、接口、变量、类型、模块、枚举上。在源码定义处添加注解后，编译工具会在使用处检查潜在的兼容性问题。当minApiVersion大于build-profile.json5中指定的compatibleSDKVersion字段，会生成兼容性警告。 |

