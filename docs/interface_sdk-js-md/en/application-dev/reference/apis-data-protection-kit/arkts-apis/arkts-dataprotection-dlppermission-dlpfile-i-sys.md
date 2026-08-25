# DLPFile (System API)

Provides APIs for managing DLP files. A **DLPFile** instance indicates a DLP file object. You can use [generateDLPFile](arkts-dataprotection-dlppermission-generatedlpfile-f-sys.md) or [openDLPFile](arkts-dataprotection-dlppermission-opendlpfile-f-sys.md) to obtain a **DLPFile** instance. The **DLPFile** object represents an opened DLP file handle, which encapsulates all operation APIs for DLP files. After using the object, the system must call the [closeDLPFile](#closedlpfile) API to release resources to prevent file handle leaks. Authorization is required when the **DLPFile** object is transferred across processes.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
```

## addDLPLinkFile

```TypeScript
addDLPLinkFile(linkFileName: string): Promise<void>
```

Adds a link file to the Filesystem in Userspace (FUSE). FUSE allows you to implement custom logic of the file system in user space. The link file is a virtual file in the FUSE, which is used to map to the DLP file. The read and write on the link file will be synchronized to the actual DLP file. This API uses a promise to return the result.After calling **addDLPLinkFile** to add a link file, the system needs to call [deleteDLPLinkFile](#deletedlplinkfile) to remove the DLP link file.When a DLP application needs to access a DLP file using a standard file API, it can add a link file as the virtual plaintext file to map the DLP file, and then perform read and write on the link file as it does on a common file.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Required permissions:** ohos.permission.ACCESS_DLP_FILE

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| linkFileName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100009](../errorcode-dlp.md#19100009-failed-to-operate-the-dlp-file) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

**Examples**

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  let uri = 'file://docs/storage/Users/currentUser/Desktop/test.txt.dlp';
  let file: number | undefined = undefined;
  let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
  let appId = '';
  let bundleName = 'com.ohos.note';
  let userId = 100;
  let dlpFile: dlpPermission.DLPFile | undefined = undefined;

  try {
    let data = bundleManager.getBundleInfoSync(bundleName, bundleFlags, userId);
    appId = data.signatureInfo.appId;
  } catch (err) {
    console.error('error', err.code, err.message);
    return;
  }

  try {
    file = fileIo.openSync(uri).fd;
    dlpFile = await dlpPermission.openDLPFile(file, appId); // Open a DLP file.
    await dlpFile.addDLPLinkFile('test.txt.dlp.link'); // Add a link file.
  } catch (err) {
    console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
  } finally {
    dlpFile?.closeDLPFile(); // Close the DLP object.
    if (file) {
      fileIo.closeSync(file);
    }
  }
}
```

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  let uri = 'file://docs/storage/Users/currentUser/Desktop/test.txt.dlp';
  let file: number | undefined = undefined;
  let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
  let appId = '';
  let bundleName = 'com.ohos.note';
  let userId = 100;
  let dlpFile: dlpPermission.DLPFile | undefined = undefined;

  try {
    let data = bundleManager.getBundleInfoSync(bundleName, bundleFlags, userId);
    appId = data.signatureInfo.appId;
  } catch (err) {
    console.error('error', err.code, err.message);
  }

  try {
    file = fileIo.openSync(uri).fd;
    dlpFile = await dlpPermission.openDLPFile(file, appId); // Open a DLP file.
    dlpFile.addDLPLinkFile('test.txt.dlp.link', async (err, res) => {
      if (err !== undefined) {
        console.error('addDLPLinkFile error,', err.code, err.message);
      } else {
        console.info('res', JSON.stringify(res));
      }
      await dlpFile?.closeDLPFile(); // Close the DLP object.
      fileIo.closeSync(file);
    });
  } catch (err) {
    console.error('addDLPLinkFile error,', (err as BusinessError).code, (err as BusinessError).message);
    await dlpFile?.closeDLPFile(); // Close the DLP object.
    if (file) {
      fileIo.closeSync(file);
    }
  }
}
```

## addDLPLinkFile

```TypeScript
addDLPLinkFile(linkFileName: string, callback: AsyncCallback<void>): void
```

Adds a link file to the FUSE. This API uses an asynchronous callback to return the result. After this API is successfully called, a virtual file used to map the DLP file is created in the FUSE.After calling **addDLPLinkFile** to add a link file, the system needs to call [deleteDLPLinkFile](#deletedlplinkfile) to remove the DLP link file.This API is called when a DLP application needs to access a DLP file using a standard file API.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Required permissions:** ohos.permission.ACCESS_DLP_FILE

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| linkFileName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100009](../errorcode-dlp.md#19100009-failed-to-operate-the-dlp-file) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

**Examples**

See [addDLPLinkFile](#adddlplinkfile)

## closeDLPFile

```TypeScript
closeDLPFile(): Promise<void>
```

Closes a **DLPFile** object. This API uses a promise to return the result.After calling [openDLPFile](arkts-dataprotection-dlppermission-opendlpfile-f-sys.md) to return a **DLPFile** object, the system must call **closeDLPFile()** to release resources after using the object.This API is used when the file owner decides to close a DLP file.

> **NOTE：**&gt;
> If a DLP file is no longer used, close the **dlpFile** object to release the memory.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Required permissions:** ohos.permission.ACCESS_DLP_FILE

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100009](../errorcode-dlp.md#19100009-failed-to-operate-the-dlp-file) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

**Examples**

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  let uri = 'file://docs/storage/Users/currentUser/Desktop/test.txt.dlp';
  let file: number | undefined = undefined;
  let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
  let appId = '';
  let bundleName = 'com.ohos.note';
  let userId = 100;
  let dlpFile: dlpPermission.DLPFile | undefined = undefined;

  try {
    let data = bundleManager.getBundleInfoSync(bundleName, bundleFlags, userId);
    appId = data.signatureInfo.appId;
  } catch (err) {
    console.error('error', err.code, err.message);
  }

  try {
    file = fileIo.openSync(uri).fd;
    dlpFile = await dlpPermission.openDLPFile(file, appId); // Open a DLP file.
  } catch (err) {
    console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
  } finally {
    dlpFile?.closeDLPFile(); // Close the DLP object.
    if (file) {
      fileIo.closeSync(file);
    }
  }
}
```

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  let uri = 'file://docs/storage/Users/currentUser/Desktop/test.txt.dlp';
  let file: number | undefined = undefined;
  let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
  let appId = '';
  let bundleName = 'com.ohos.note';
  let userId = 100;
  let dlpFile: dlpPermission.DLPFile | undefined = undefined;

  try {
    let data = bundleManager.getBundleInfoSync(bundleName, bundleFlags, userId);
    appId = data.signatureInfo.appId;
  } catch (err) {
    console.error('error', err.code, err.message);
  }

  try {
    file = fileIo.openSync(uri).fd;
    dlpFile = await dlpPermission.openDLPFile(file, appId); // Open a DLP file.
    dlpFile.closeDLPFile((err, res) => {// Close the DLP file.
      if (err !== undefined) {
        console.error('closeDLPFile error,', err.code, err.message);
      } else {
        console.info('res', JSON.stringify(res));
      }
      fileIo.closeSync(file);
    });
  } catch (err) {
    console.error('error,', (err as BusinessError).code, (err as BusinessError).message);
    if (file) {
      fileIo.closeSync(file);
    }
  }
}
```

## closeDLPFile

```TypeScript
closeDLPFile(callback: AsyncCallback<void>): void
```

Closes a **DLPFile** object. This API uses an asynchronous callback to return the result.After calling **openDLPFile()** to return a **DLPFile** object, the system must call **closeDLPFile()** to release resources after using the object.This API is used when the file owner decides to close a DLP file.

> **NOTE：**&gt;
> If a DLP file is no longer used, close the **dlpFile** instance to release the memory.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Required permissions:** ohos.permission.ACCESS_DLP_FILE

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100009](../errorcode-dlp.md#19100009-failed-to-operate-the-dlp-file) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

**Examples**

See [closeDLPFile](#closedlpfile)

## deleteDLPLinkFile

```TypeScript
deleteDLPLinkFile(linkFileName: string): Promise<void>
```

Deletes a link file from the FUSE. This API uses a promise to return the result. After the API is successfully called, the specified link file is deleted from the FUSE.Before calling **deleteDLPLinkFile**, the system must call [addDLPLinkFile](#adddlplinkfile) to add a DLP link file.This API is used to clear the link file mapping after DLP file access is complete.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Required permissions:** ohos.permission.ACCESS_DLP_FILE

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| linkFileName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100009](../errorcode-dlp.md#19100009-failed-to-operate-the-dlp-file) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

**Examples**

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  let uri = 'file://docs/storage/Users/currentUser/Desktop/test.txt.dlp';
  let file: number | undefined = undefined;
  let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
  let appId = '';
  let bundleName = 'com.ohos.note';
  let userId = 100;
  let dlpFile: dlpPermission.DLPFile | undefined = undefined;

  try {
    let data = bundleManager.getBundleInfoSync(bundleName, bundleFlags, userId);
    appId = data.signatureInfo.appId;
  } catch (err) {
    console.error('error', err.code, err.message);
  }

  try {
    file = fileIo.openSync(uri).fd;
    dlpFile = await dlpPermission.openDLPFile(file, appId); // Open a DLP file.
    await dlpFile.addDLPLinkFile('test.txt.dlp.link'); // Add a link file.
    await dlpFile.deleteDLPLinkFile('test.txt.dlp.link'); // Delete a link file.
  } catch (err) {
    console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
  } finally {
    await dlpFile?.closeDLPFile(); // Close the DLP object.
    if (file) {
      fileIo.closeSync(file);
    }
  }
}
```

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  let uri = 'file://docs/storage/Users/currentUser/Desktop/test.txt.dlp';
  let file: number | undefined = undefined;
  let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
  let appId = '';
  let bundleName = 'com.ohos.note';
  let userId = 100;
  let dlpFile: dlpPermission.DLPFile | undefined = undefined;

  try {
    let data = bundleManager.getBundleInfoSync(bundleName, bundleFlags, userId);
    appId = data.signatureInfo.appId;
  } catch (err) {
    console.error('error', err.code, err.message);
  }

  try {
    file = fileIo.openSync(uri).fd;
    dlpFile = await dlpPermission.openDLPFile(file, appId); // Open a DLP file.
    await dlpFile.addDLPLinkFile('test.txt.dlp.link'); // Add a link file.
    dlpFile.deleteDLPLinkFile('test.txt.dlp.link', async (err, res) => { // Delete a link file.
      if (err !== undefined) {
        console.error('deleteDLPLinkFile error,', err.code, err.message);
      } else {
        console.info('res', JSON.stringify(res));
      }
      await dlpFile?.closeDLPFile(); // Close the DLP object.
      fileIo.closeSync(file);
    });
  } catch (err) {
    console.error('error,', (err as BusinessError).code, (err as BusinessError).message);
    await dlpFile?.closeDLPFile(); // Close the DLP object.
    if (file) {
      fileIo.closeSync(file);
    }
  }
}
```

## deleteDLPLinkFile

```TypeScript
deleteDLPLinkFile(linkFileName: string, callback: AsyncCallback<void>): void
```

Deletes a link file from the FUSE. This API uses an asynchronous callback to return the result. After the API is successfully called, the specified link file is deleted from the FUSE.Before calling **deleteDLPLinkFile**, the system must call [addDLPLinkFile](#adddlplinkfile) to add a DLP link file.This API is used to clear the link file mapping after DLP file access is complete.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Required permissions:** ohos.permission.ACCESS_DLP_FILE

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| linkFileName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100009](../errorcode-dlp.md#19100009-failed-to-operate-the-dlp-file) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

**Examples**

See [deleteDLPLinkFile](#deletedlplinkfile)

## recoverDLPFile

```TypeScript
recoverDLPFile(plaintextFd: number): Promise<void>
```

Recovers the plaintext of a DLP file. This API uses a promise to return the result.This API is used when the file owner decides to disable the DLP protection for a file and convert it into a common file for free sharing.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Required permissions:** ohos.permission.ACCESS_DLP_FILE

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| plaintextFd | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100002](../errorcode-dlp.md#19100002-encryption-and-decryption-error) |
| [19100003](../errorcode-dlp.md#19100003-encryptiondecryption-timeout) |
| [19100004](../errorcode-dlp.md#19100004-credential-service-error) |
| [19100005](../errorcode-dlp.md#19100005-credential-authentication-server-error) |
| [19100008](../errorcode-dlp.md#19100008-non-dlp-file) |
| [19100009](../errorcode-dlp.md#19100009-failed-to-operate-the-dlp-file) |
| [19100010](../errorcode-dlp.md#19100010-read-only-dlp-file) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

**Examples**

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  let uri = 'file://docs/storage/Users/currentUser/Desktop/test.txt.dlp';
  let file: number | undefined = undefined;
  let destFile: number | undefined = undefined;
  let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
  let appId = '';
  let bundleName = 'com.ohos.note';
  let userId = 100;
  let dlpFile: dlpPermission.DLPFile | undefined = undefined;

  try {
    let data = bundleManager.getBundleInfoSync(bundleName, bundleFlags, userId);
    appId = data.signatureInfo.appId;
  } catch (err) {
    console.error('error', err.code, err.message);
  }

  try {
    file = fileIo.openSync(uri).fd;
    destFile = fileIo.openSync('destUri').fd;
    dlpFile = await dlpPermission.openDLPFile(file, appId); // Open a DLP file.
    await dlpFile.recoverDLPFile(destFile); // Recover the plaintext of a DLP file.
  } catch (err) {
    console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
  } finally {
    dlpFile?.closeDLPFile(); // Close the DLP object.
    if (file) {
      fileIo.closeSync(file);
    }
    if (destFile) {
      fileIo.closeSync(destFile);
    }
  }
}
```

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  let uri = 'file://docs/storage/Users/currentUser/Desktop/test.txt.dlp';
  let file: number | undefined = undefined;
  let destFile: number | undefined = undefined;
  let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
  let appId = '';
  let bundleName = 'com.ohos.note';
  let userId = 100;
  let dlpFile: dlpPermission.DLPFile | undefined = undefined;

  try {
    let data = bundleManager.getBundleInfoSync(bundleName, bundleFlags, userId);
    appId = data.signatureInfo.appId;
  } catch (err) {
    console.error('error', err.code, err.message);
  }

  try {
    file = fileIo.openSync(uri).fd;
    destFile = fileIo.openSync('destUri').fd;
    dlpFile = await dlpPermission.openDLPFile(file, appId); // Open a DLP file.
    dlpFile.recoverDLPFile(destFile, async (err, res) => { // Recover the plaintext of a DLP file.
      if (err !== undefined) {
        console.error('recoverDLPFile error,', err.code, err.message);
      } else {
        console.info('res', JSON.stringify(res));
      }
      await dlpFile?.closeDLPFile(); // Close the DLP object.
      fileIo.closeSync(file);
      fileIo.closeSync(destFile);
    });
  } catch (err) {
    console.error('error,', (err as BusinessError).code, (err as BusinessError).message);
    await dlpFile?.closeDLPFile(); // Close the DLP object.
    if (file) {
      fileIo.closeSync(file);
    }
    if (destFile) {
      fileIo.closeSync(destFile);
    }
  }
}
```

## recoverDLPFile

```TypeScript
recoverDLPFile(plaintextFd: number, callback: AsyncCallback<void>): void
```

Recovers the plaintext of a DLP file. This API uses an asynchronous callback to return the result.This API is used when the file owner decides to disable the DLP protection for a file.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Required permissions:** ohos.permission.ACCESS_DLP_FILE

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| plaintextFd | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100002](../errorcode-dlp.md#19100002-encryption-and-decryption-error) |
| [19100003](../errorcode-dlp.md#19100003-encryptiondecryption-timeout) |
| [19100004](../errorcode-dlp.md#19100004-credential-service-error) |
| [19100005](../errorcode-dlp.md#19100005-credential-authentication-server-error) |
| [19100008](../errorcode-dlp.md#19100008-non-dlp-file) |
| [19100009](../errorcode-dlp.md#19100009-failed-to-operate-the-dlp-file) |
| [19100010](../errorcode-dlp.md#19100010-read-only-dlp-file) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

**Examples**

See [recoverDLPFile](#recoverdlpfile)

## replaceDLPLinkFile

```TypeScript
replaceDLPLinkFile(linkFileName: string): Promise<void>
```

Replaces a link file. This API uses a promise to return the result. After the API is successfully called, the current link file is replaced with the new link file. Before performing this operation, you need to create a link file and stop the read and write operation on the FUSE.When you need to access a different DLP file, you can replace the link file to change the file mapping.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Required permissions:** ohos.permission.ACCESS_DLP_FILE

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| linkFileName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100009](../errorcode-dlp.md#19100009-failed-to-operate-the-dlp-file) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

**Examples**

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  let uri = 'file://docs/storage/Users/currentUser/Desktop/test.txt.dlp';
  let file: number | undefined = undefined;
  let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
  let appId = '';
  let bundleName = 'com.ohos.note';
  let userId = 100;
  let dlpFile: dlpPermission.DLPFile | undefined = undefined;

  try {
    let data = bundleManager.getBundleInfoSync(bundleName, bundleFlags, userId);
    appId = data.signatureInfo.appId;
  } catch (err) {
    console.error('error', err.code, err.message);
  }

  try {
    file = fileIo.openSync(uri).fd;
    dlpFile = await dlpPermission.openDLPFile(file, appId); // Open a DLP file.
    await dlpFile.addDLPLinkFile('test.txt.dlp.link'); // Add a link file.
    await dlpFile.stopFuseLink(); // Stop the read and write on the FUSE.
    await dlpFile.replaceDLPLinkFile('test_new.txt.dlp.link'); // Replace a link file.
    await dlpFile.resumeFuseLink(); // Resume read/write on the link file.
  } catch (err) {
    console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
  } finally {
    await dlpFile?.closeDLPFile(); // Close the DLP object.
    if (file) {
      fileIo.closeSync(file);
    }
  }
}
```

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  let uri = 'file://docs/storage/Users/currentUser/Desktop/test.txt.dlp';
  let file: number | undefined = undefined;
  let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
  let appId = '';
  let bundleName = 'com.ohos.note';
  let userId = 100;
  let dlpFile: dlpPermission.DLPFile | undefined = undefined;

  try {
    let data = bundleManager.getBundleInfoSync(bundleName, bundleFlags, userId);
    appId = data.signatureInfo.appId;
  } catch (err) {
    console.error('error', err.code, err.message);
  }

  try {
    file = fileIo.openSync(uri).fd;
    dlpFile = await dlpPermission.openDLPFile(file, appId); // Open a DLP file.
    await dlpFile.addDLPLinkFile('test.txt.dlp.link'); // Add a link file.
    await dlpFile.stopFuseLink(); // Stop the read and write on the FUSE.
    dlpFile.replaceDLPLinkFile('test_new.txt.dlp.link', async (err, res) => { // Replace a link file.
      if (err !== undefined) {
        console.error('replaceDLPLinkFile error,', err.code, err.message);
      } else {
        console.info('res', JSON.stringify(res));
        await dlpFile?.resumeFuseLink(); // Resume the read and write on the FUSE.
      }
      await dlpFile?.closeDLPFile(); // Close the DLP object.
      fileIo.closeSync(file);
    });
  } catch (err) {
    console.error('error,', (err as BusinessError).code, (err as BusinessError).message);
    await dlpFile?.closeDLPFile(); // Close the DLP object.
    if (file) {
      fileIo.closeSync(file);
    }
  }
}
```

## replaceDLPLinkFile

```TypeScript
replaceDLPLinkFile(linkFileName: string, callback: AsyncCallback<void>): void
```

Replaces a link file. This API uses an asynchronous callback to return the result. After the API is successfully called, the current link file is replaced with the new link file.When you need to access a different DLP file, you can replace the link file. Before performing this operation, you need to create a link file and stop the read and write operation on the FUSE.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Required permissions:** ohos.permission.ACCESS_DLP_FILE

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| linkFileName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100009](../errorcode-dlp.md#19100009-failed-to-operate-the-dlp-file) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

**Examples**

See [replaceDLPLinkFile](#replacedlplinkfile)

## resumeFuseLink

```TypeScript
resumeFuseLink(): Promise<void>
```

Resumes the read and write on the FUSE. This API uses a promise to return the result. After the API is successfully called, the read and write on the link file are resumed.This API can be called to resume read and write only after [stopFuseLink](#stopfuselink) is called to stop the read and write operations.After the link file is replaced, the read and write need to be resumed for normal file access.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Required permissions:** ohos.permission.ACCESS_DLP_FILE

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100009](../errorcode-dlp.md#19100009-failed-to-operate-the-dlp-file) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

**Examples**

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  let uri = 'file://docs/storage/Users/currentUser/Desktop/test.txt.dlp';
  let file: number | undefined = undefined;
  let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
  let appId = '';
  let bundleName = 'com.ohos.note';
  let userId = 100;
  let dlpFile: dlpPermission.DLPFile | undefined = undefined;

  try {
    let data = bundleManager.getBundleInfoSync(bundleName, bundleFlags, userId);
    appId = data.signatureInfo.appId;
  } catch (err) {
    console.error('error', err.code, err.message);
  }

  try {
    file = fileIo.openSync(uri).fd;
    dlpFile = await dlpPermission.openDLPFile(file, appId); // Open a DLP file.
    await dlpFile.addDLPLinkFile('test.txt.dlp.link'); // Add a link file.
    await dlpFile.stopFuseLink(); // Stop the read and write on the FUSE.
    await dlpFile.resumeFuseLink(); // Resume read/write on the link file.
  } catch (err) {
    console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
  } finally {
    dlpFile?.closeDLPFile(); // Close the DLP object.
    if (file) {
      fileIo.closeSync(file);
    }
  }
}
```

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  let uri = 'file://docs/storage/Users/currentUser/Desktop/test.txt.dlp';
  let file: number | undefined = undefined;
  let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
  let appId = '';
  let bundleName = 'com.ohos.note';
  let userId = 100;
  let dlpFile: dlpPermission.DLPFile | undefined = undefined;

  try {
    let data = bundleManager.getBundleInfoSync(bundleName, bundleFlags, userId);
    appId = data.signatureInfo.appId;
  } catch (err) {
    console.error('error', err.code, err.message);
  }

  try {
    file = fileIo.openSync(uri).fd;
    dlpFile = await dlpPermission.openDLPFile(file, appId); // Open a DLP file.
    await dlpFile.addDLPLinkFile('test.txt.dlp.link'); // Add a link file.
    await dlpFile.stopFuseLink(); // Stop the read and write on the FUSE.
    dlpFile.resumeFuseLink(async (err, res) => {
      if (err !== undefined) {
        console.error('resumeFuseLink error,', err.code, err.message);
      } else {
        console.info('res', JSON.stringify(res));
      }
      await dlpFile?.closeDLPFile(); // Close the DLP object.
      fileIo.closeSync(file);
    });
  } catch (err) {
    console.error('resumeFuseLink error,', (err as BusinessError).code, (err as BusinessError).message);
    await dlpFile?.closeDLPFile(); // Close the DLP object.
    if (file) {
      fileIo.closeSync(file);
    }
  }
}
```

## resumeFuseLink

```TypeScript
resumeFuseLink(callback: AsyncCallback<void>): void
```

Resumes the read and write on the FUSE. This API uses an asynchronous callback to return the result. After the API is successfully called, the read and write on the link file are resumed.This API can be called to resume read and write only after [stopFuseLink](#stopfuselink) is called to stop the read and write operations.After the link file is replaced, the read and write need to be resumed.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Required permissions:** ohos.permission.ACCESS_DLP_FILE

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100009](../errorcode-dlp.md#19100009-failed-to-operate-the-dlp-file) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

**Examples**

See [resumeFuseLink](#resumefuselink)

## stopFuseLink

```TypeScript
stopFuseLink(): Promise<void>
```

Stops the read and write on the FUSE. This API uses a promise to return the result. After the API is successfully called, the read and write on the link file are stopped.After calling **stopFuseLink** to stop the read and write operations on the FUSE, the system must call [resumeFuseLink](#resumefuselink) to resume the read and write operations.Before deleting a link file, stop the read and write to ensure secure file operations.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Required permissions:** ohos.permission.ACCESS_DLP_FILE

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100009](../errorcode-dlp.md#19100009-failed-to-operate-the-dlp-file) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

**Examples**

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  let uri = 'file://docs/storage/Users/currentUser/Desktop/test.txt.dlp';
  let file: number | undefined = undefined;
  let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
  let appId = '';
  let bundleName = 'com.ohos.note';
  let userId = 100;
  let dlpFile: dlpPermission.DLPFile | undefined = undefined;

  try {
    let data = bundleManager.getBundleInfoSync(bundleName, bundleFlags, userId);
    appId = data.signatureInfo.appId;
  } catch (err) {
    console.error('error', err.code, err.message);
  }

  try {
    file = fileIo.openSync(uri).fd;
    dlpFile = await dlpPermission.openDLPFile(file, appId) // Open a DLP file.
    dlpFile.addDLPLinkFile('test.txt.dlp.link'); // Add a link file.
    dlpFile.stopFuseLink(); // Stop read/write on the link file.
  } catch (err) {
    console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
  } finally {
    dlpFile?.closeDLPFile(); // Close the DLP object.
    if (file) {
      fileIo.closeSync(file);
    }
  }
}
```

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  let uri = 'file://docs/storage/Users/currentUser/Desktop/test.txt.dlp';
  let file: number | undefined = undefined;
  let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
  let appId = '';
  let bundleName = 'com.ohos.note';
  let userId = 100;
  let dlpFile: dlpPermission.DLPFile | undefined = undefined;

  try {
    let data = bundleManager.getBundleInfoSync(bundleName, bundleFlags, userId);
    appId = data.signatureInfo.appId;
  } catch (err) {
    console.error('error', err.code, err.message);
  }

  try {
    file = fileIo.openSync(uri).fd;
    dlpFile = await dlpPermission.openDLPFile(file, appId); // Open a DLP file.
    await dlpFile.addDLPLinkFile('test.txt.dlp.link'); // Add a link file.
    dlpFile.stopFuseLink(async (err, res) => {
      if (err !== undefined) {
        console.error('stopFuseLink error,', err.code, err.message);
      } else {
        console.info('res', JSON.stringify(res));
      }
      await dlpFile?.closeDLPFile(); // Close the DLP object.
      fileIo.closeSync(file);
    });
  } catch (err) {
    console.error('stopFuseLink error,', (err as BusinessError).code, (err as BusinessError).message);
    await dlpFile?.closeDLPFile(); // Close the DLP object.
    if (file) {
      fileIo.closeSync(file);
    }
  }
}
```

## stopFuseLink

```TypeScript
stopFuseLink(callback: AsyncCallback<void>): void
```

Stops the read and write on the FUSE. This API uses an asynchronous callback to return the result. After the API is successfully called, the read and write on the link file are stopped.After calling **stopFuseLink** to stop the read and write operations on the FUSE, the system must call [resumeFuseLink](#resumefuselink) to resume the read and write operations.Before deleting a link file, stop the read and write.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Required permissions:** ohos.permission.ACCESS_DLP_FILE

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100009](../errorcode-dlp.md#19100009-failed-to-operate-the-dlp-file) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

**Examples**

See [stopFuseLink](#stopfuselink)

## dlpProperty

```TypeScript
dlpProperty: DLPProperty
```

Authorized user information.

**Type:** [DLPProperty](arkts-dataprotection-dlppermission-dlpproperty-i.md)

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.
