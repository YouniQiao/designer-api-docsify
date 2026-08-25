# @ohos.nearlink.ssap(星闪SSAP连接能力)

本模块提供了SSAP（星闪服务交互协议 SparkLink Service Access Protocol）连接功能，包括客户端创建与连接、调用服务端方法、读写描述符、订阅事件通知等。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Base

## 导入模块

```TypeScript
import { ssap } from '@kit.ConnectivityKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [createClient(星闪SSAP连接能力)](arkts-connectivity-ssap-createclient-f.md) |
| [createServer(星闪SSAP连接能力)](arkts-connectivity-ssap-createserver-f.md) |

### 接口

| 名称 |
| --- |
| [Client(星闪SSAP连接能力)](arkts-connectivity-ssap-client-i.md) |
| [ConnectionChangeState(星闪SSAP连接能力)](arkts-connectivity-ssap-connectionchangestate-i.md) |
| [Property(星闪SSAP连接能力)](arkts-connectivity-ssap-property-i.md) |
| [PropertyDescriptor(星闪SSAP连接能力)](arkts-connectivity-ssap-propertydescriptor-i.md) |
| [PropertyReadRequest(星闪SSAP连接能力)](arkts-connectivity-ssap-propertyreadrequest-i.md) |
| [PropertyWriteRequest(星闪SSAP连接能力)](arkts-connectivity-ssap-propertywriterequest-i.md) |
| [Server(星闪SSAP连接能力)](arkts-connectivity-ssap-server-i.md) |
| [ServerResponse(星闪SSAP连接能力)](arkts-connectivity-ssap-serverresponse-i.md) |
| [Service(星闪SSAP连接能力)](arkts-connectivity-ssap-service-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [Client(星闪SSAP连接能力)](arkts-connectivity-ssap-client-i-sys.md) |
| [Event(星闪SSAP连接能力)](arkts-connectivity-ssap-event-i-sys.md) |
| [Method(星闪SSAP连接能力)](arkts-connectivity-ssap-method-i-sys.md) |
| [Service(星闪SSAP连接能力)](arkts-connectivity-ssap-service-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [Operation(星闪SSAP连接能力)](arkts-connectivity-ssap-operation-e.md) |
| [PropertyDescriptorType(星闪SSAP连接能力)](arkts-connectivity-ssap-propertydescriptortype-e.md) |
| [PropertyWriteType(星闪SSAP连接能力)](arkts-connectivity-ssap-propertywritetype-e.md) |

### 类型

| 名称 |
| --- |
| [ConnectionState(星闪SSAP连接能力)](arkts-connectivity-ssap-connectionstate-t.md) |
