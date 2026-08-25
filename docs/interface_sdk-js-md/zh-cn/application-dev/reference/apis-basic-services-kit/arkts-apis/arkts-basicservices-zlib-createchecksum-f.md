# createChecksum

## 导入模块

```TypeScript
import { zlib } from 'kits/@kit.BasicServicesKit';
```

## createChecksum

```TypeScript
function createChecksum(): Promise<Checksum>
```

创建校验对象。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Checksum](arkts-basicservices-zlib-checksum-i.md)&gt; |
