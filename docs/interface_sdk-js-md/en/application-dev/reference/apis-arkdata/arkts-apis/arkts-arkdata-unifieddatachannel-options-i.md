# Options

UDMF提供的数据操作接口包含三个可选参数：intention、key和visibility。如果接口不需要这些参数，可以不填，具体要求请参阅该接口的参数说明。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unifiedDataChannel-interface Options--><!--Device-unifiedDataChannel-interface Options-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { unifiedDataChannel } from 'kits/@kit.ArkData';
```

## intention

```TypeScript
intention?: Intention
```

表示数据操作相关的数据通路类型，取值为[Intention](arkts-arkdata-unifieddatachannel-intention-e.md)枚举类型，包括DATA_HUB、DRAG等。不填写时默认无值，具体是否必填请参阅具体接口的参数说明。

**Type:** [Intention](arkts-arkdata-unifieddatachannel-intention-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Options-intention?: Intention--><!--Device-Options-intention?: Intention-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## key

```TypeScript
key?: string
```

UDMF中数据对象的唯一标识符，可通过[insertData](arkts-arkdata-unifieddatachannel-insertdata-f.md#insertdata)接口的返回值获取。不填写时默认无值，具体是否必填请参阅具体接口的参数说明。

由udmf:/、intention、bundleName和groupId四部分组成，以'/'连接，比如：udmf://DataHub/com.ohos.test/0123456789。

其中udmf:/固定，DataHub为对应枚举的取值，com.ohos.test为包名，0123456789为随机生成的groupId。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Options-key?: string--><!--Device-Options-key?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## visibility

```TypeScript
visibility?: Visibility
```

表示数据的可见性等级，仅公共数据通路可使用，取值为[Visibility](arkts-arkdata-unifieddatachannel-visibility-e.md)枚举类型。只在写入数据的时候填写才生效，若不填写默认是Visibility.ALL。

**Type:** [Visibility](../../apis-arkui/arkts-apis/arkts-arkui-visibility-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Options-visibility?: Visibility--><!--Device-Options-visibility?: Visibility-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

