#!/bin/bash
CONTAINER=$1
ZIP_PATH=$2
DB_PASSWORD=$3
ZIP_NAME=$(basename $ZIP_PATH)
TEMP_DIR=$(mktemp -d)

# Extract ZIP
unzip -q $ZIP_PATH -d $TEMP_DIR

# Inject password into sqlalchemy_uri
find $TEMP_DIR -name "*.yaml" | while read f; do
  sed -i "s|analyst:XXXXXXXXXX@|analyst:$DB_PASSWORD@|g" $f
done

# Repack ZIP
cd $TEMP_DIR && zip -qr /tmp/$ZIP_NAME . && cd -

# Copy and import
docker cp /tmp/$ZIP_NAME $CONTAINER:/tmp/$ZIP_NAME
docker exec $CONTAINER superset import-dashboards -p /tmp/$ZIP_NAME -u admin

# Cleanup
rm -rf $TEMP_DIR /tmp/$ZIP_NAME
