# This file is really only useful for testing code, but it will
# get you started. That said, you'll be much better off setting 
# up dockerMan or docker-compose

echo "-- Stopping --"
docker stop harmonyonenotifier || true
echo "-- Cleaning --"
docker rm harmonyonenotifier || true
echo "-- Building --"
docker build . -t lnxd/harmonyonenotifier
echo "-- Running --"
docker run -ti --name harmonyonenotifier \
       --env NOTIFIER_API_APP=agmie86vk8krumow4tpc5rfyq315f8 \
       --env NOTIFIER_API_USER=x \
       --env HARMONYONE_WALLET=one1wksazguqkyty7wdty6786wp0k9gllmvyjn2ka0 \
       lnxd/harmonyonenotifier