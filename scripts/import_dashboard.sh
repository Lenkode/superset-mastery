#!/bin/bash
CONTAINER=$1
ZIP_PATH=$2
DB_PASSWORD=$3
ZIP_NAME=$(basename $ZIP_PATH)
TEMP_DIR=$(mktemp -d)

unzip -q $ZIP_PATH -d $TEMP_DIR

find $TEMP_DIR -name "*.yaml" | xargs grep -l "password:" | while read f; do
  sed -i "s/password: null/password: $DB_PASSWORD/" $f
  sed -i "s/password: ''/password: $DB_PASSWORD/" $f
done

cd $TEMP_DIR && zip -qr /tmp/$ZIP_NAME . && cd -

docker cp /tmp/$ZIP_NAME $CONTAINER:/tmp/$ZIP_NAME
docker exec $CONTAINER superset import-dashboards -p /tmp/$ZIP_NAME -u admin

rm -rf $TEMP_DIR /tmp/$ZIP_NAME
