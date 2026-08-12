# @ohos.data.distributedDataObject

The distributedDataObject module provides basic data object management, including creating, querying, deleting,modifying, and subscribing to data objects, and distributed data object collaboration for the same application among multiple devices. Although this module does not parse user data, you are advised not to transfer sensitive personal data or privacy data due to low-level security of storage path.

**Since:** 8

<!--Device-unnamed-declare namespace distributedDataObject--><!--Device-unnamed-declare namespace distributedDataObject-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

## Modules to Import

```TypeScript
import { distributedDataObject } from '@kit.ArkData';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [create](arkts-arkdata-distributeddataobject-create-f.md#create) |
| [createDistributedObject](arkts-arkdata-distributeddataobject-createdistributedobject-f.md#createdistributedobject) |
| [genSessionId](arkts-arkdata-distributeddataobject-gensessionid-f.md#gensessionid) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BindInfo](arkts-arkdata-distributeddataobject-bindinfo-i.md) |
| [DataObject](arkts-arkdata-distributeddataobject-dataobject-i.md) |
| [DistributedObject](arkts-arkdata-distributeddataobject-distributedobject-i.md) |
| [RevokeSaveSuccessResponse](arkts-arkdata-distributeddataobject-revokesavesuccessresponse-i.md) |
| [SaveSuccessResponse](arkts-arkdata-distributeddataobject-savesuccessresponse-i.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DataObserver](arkts-arkdata-distributeddataobject-dataobserver-t.md) |
| [ProgressObserver](arkts-arkdata-distributeddataobject-progressobserver-t.md) |
| [StatusObserver](arkts-arkdata-distributeddataobject-statusobserver-t.md) |
